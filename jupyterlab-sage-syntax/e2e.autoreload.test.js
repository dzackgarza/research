import { test, expect } from "@playwright/test";
import { writeFileSync, unlinkSync, existsSync } from "node:fs";
import { join } from "node:path";
import { randomBytes } from "node:crypto";

/**
 * Regression tests for the auto-reload plugin
 * (@dzack/jupyterlab-sage-syntax:auto-reload).
 *
 * These exercise the two branches of `checkForDiskChange` against the live
 * JupyterLab server at http://localhost:8888, whose root_dir is
 * /home/dzack/research/computations/notebooks. Each test creates a throwaway
 * fixture under that root, drives the real file editor, mutates the file on
 * disk, and asserts the owned behavior:
 *
 *   1. A clean editor reverts to the on-disk version automatically.
 *   2. A dirty editor shows the "File Changed on Disk" confirmation dialog
 *      with Keep Editing / Reload from Disk actions.
 *
 * Both would fail against the gutted stub (no polling interval, no
 * fileChanged signal, no showDialog call) that was committed in 5aa93bf and
 * restored in the fix.
 */

const serverRoot = "/home/dzack/research/computations/notebooks";
const baseUrl = "http://localhost:8888/lab/tree";

function uniqueMarker(label) {
  return `${label}-${randomBytes(4).toString("hex")}`;
}

function fixturePath(name) {
  return join(serverRoot, name);
}

async function openFileInEditor(page, relPath) {
  await page.goto(`${baseUrl}/${relPath}`, { waitUntil: "domcontentloaded" });
  await page
    .locator("#jp-main-dock-panel")
    .waitFor({ state: "attached", timeout: 30000 });
  await page
    .locator(".cm-editor")
    .first()
    .waitFor({ state: "attached", timeout: 30000 });
  // Settle period matching the existing e2e convention so the editor
  // finishes loading the document model and the auto-reload interval starts.
  await page.waitForTimeout(4000);
}

async function activeEditor(page) {
  const editorIndex = await page
    .locator(".cm-editor")
    .evaluateAll((editors) => {
      const visible = editors
        .map((editor, index) => ({ editor, index }))
        .filter(({ editor }) => {
          const rect = editor.getBoundingClientRect();
          const style = getComputedStyle(editor);
          return (
            rect.width > 0 &&
            rect.height > 0 &&
            style.display !== "none" &&
            style.visibility !== "hidden"
          );
        });
      if (visible.length !== 1) {
        throw new Error(
          `expected one visible CodeMirror editor, found ${visible.length}`,
        );
      }
      return visible[0].index;
    });
  return page.locator(".cm-editor").nth(editorIndex);
}

async function editorContent(page) {
  const editor = await activeEditor(page);
  const content = await editor.locator(".cm-content").textContent();
  return content ?? "";
}

test.describe("JupyterLab auto-reload on external file changes", () => {
  test.setTimeout(60000);

  let filePath;

  test.afterEach(() => {
    if (filePath && existsSync(filePath)) {
      try {
        unlinkSync(filePath);
      } catch {
        /* best-effort cleanup; failure is non-fatal */
      }
    }
    filePath = undefined;
  });

  test("clean editor reverts to the on-disk version after external modification", async ({
    page,
  }) => {
    const oldMarker = uniqueMarker("autoreload-clean-old");
    const newMarker = uniqueMarker("autoreload-clean-new");
    const fileName = `${uniqueMarker("test-autoreload-clean")}.py`;
    filePath = fixturePath(fileName);

    writeFileSync(filePath, `${oldMarker}\n`);

    await openFileInEditor(page, fileName);
    const before = await editorContent(page);
    expect(before, "editor must initially render the on-disk marker").toContain(
      oldMarker,
    );

    // External mutation: replace the file content on disk.
    writeFileSync(filePath, `${newMarker}\n`);

    // The plugin polls every 1000 ms; allow a generous window for the
    // contents.get round-trip, context.revert(), and CodeMirror re-render.
    await expect
      .poll(() => editorContent(page), {
        timeout: 15000,
        message: "clean editor should reload to show the new on-disk marker",
      })
      .toContain(newMarker);
  });

  test("dirty editor shows the File Changed on Disk dialog with both actions", async ({
    page,
  }) => {
    const initialMarker = uniqueMarker("autoreload-dirty-initial");
    const diskMarker = uniqueMarker("autoreload-dirty-diskchange");
    const typedMarker = uniqueMarker("autoreload-dirty-typed");
    const fileName = `${uniqueMarker("test-autoreload-dirty")}.py`;
    filePath = fixturePath(fileName);

    writeFileSync(filePath, `${initialMarker}\n`);

    await openFileInEditor(page, fileName);
    const initialContent = await editorContent(page);
    expect(initialContent).toContain(initialMarker);

    // Make the editor dirty by typing unsaved content.
    const editor = await activeEditor(page);
    await editor.click();
    await page.keyboard.press("End");
    await page.keyboard.type(`\n${typedMarker}\n`);

    const afterTyping = await editorContent(page);
    expect(
      afterTyping,
      "typed marker must be present before the disk change",
    ).toContain(typedMarker);

    // External mutation while the editor is dirty.
    writeFileSync(filePath, `${diskMarker}\n`);

    // The dirty branch calls showDialog, which renders a .jp-Dialog with the
    // configured title and buttons.
    const dialog = page
      .locator(".jp-Dialog")
      .filter({ hasText: "File Changed on Disk" });

    await expect(
      dialog,
      "the File Changed on Disk dialog must appear",
    ).toBeVisible({
      timeout: 15000,
    });
    await expect(dialog).toContainText("Keep Editing");
    await expect(dialog).toContainText("Reload from Disk");
  });
});
