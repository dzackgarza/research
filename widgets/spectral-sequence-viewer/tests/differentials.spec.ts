import { test, expect } from "@playwright/test";
import sequence from "../examples/sequence.json" with { type: "json" };
test("inspect clipped maps through all filters and zero styles", async ({
  page,
}) => {
  await page.goto("/examples/static/");
  await page.getByRole("button", { name: "(2,1)", exact: true }).click();
  const inspector = page.getByRole("region", { name: "Inspector" });
  await expect(
    inspector.getByRole("img", {
      name: /E_2\^\{0,2\}.*E_2\^\{2,1\}.*E_2\^\{4,0\}/,
    }),
  ).toBeVisible({ timeout: 2000 });
  const chain = inspector.locator(".chain > svg");
  await page.getByText("Display options", { exact: true }).click();
  for (const mode of ["All", "Potentially nonzero", "Known nonzero", "None"]) {
    await page.getByLabel("Arrows").selectOption(mode);
    await expect(chain).toHaveAccessibleName(
      /E_2\^\{0,2\}.*d_2\^\{0,2\}.*E_2\^\{2,1\}.*state-zero.*d_2\^\{2,1\}.*E_2\^\{4,0\}.*g/,
    );
    const arrows = page.locator("line[data-status]");
    if (mode === "All") await expect(arrows).toHaveCount(3);
    if (mode === "Potentially nonzero")
      await expect(arrows.filter({ visible: true })).toHaveCount(2);
    if (mode === "Known nonzero") await expect(arrows).toHaveCount(1);
    if (mode === "None") await expect(arrows).toHaveCount(0);
  }
  await page.getByLabel("Arrows").selectOption("Known nonzero");
  await page.getByRole("button", { name: "(0,1)", exact: true }).click();
  await expect(page.locator('line[data-highlighted="true"]')).toHaveCount(1);
  for (const style of ["dot", "blank", "zero"]) {
    await page.getByRole("button", { name: "Display options" }).click();
    await page.getByLabel("Zero style").selectOption(style);
    const zero = page.getByRole("button", { name: "(1,0)", exact: true });
    await zero.focus();
    await zero.press("Enter");
    await expect(chain).toHaveAccessibleName(
      /state-zero\}\{E_2\^\{1,0\}\}/,
    );
    await expect(
      page.getByRole("button", { name: "(3,1)", exact: true }),
    ).toContainText("?");
  }
  await page
    .locator("spectral-sequence-viewer")
    .evaluate((el, d) => Object.assign(el, { sequence: d }), {
      ...sequence,
      convention: "homological",
      pages: sequence.pages.map((p) => ({ ...p, maps: [] })),
    });
  await page.getByRole("button", { name: "(2,1)", exact: true }).click();
  await expect(chain).toHaveAccessibleName(
    /E\^2_\{4,0\}.*E\^2_\{2,1\}.*E\^2_\{0,2\}/,
  );
});

test("an undetermined map and a zero map can be read without colour", async ({ page }) => {
  await page.goto("/examples/static/");
  await page.getByRole("button", { name: "(2,1)", exact: true }).click();
  const chain = page.locator(".chain > svg");
  await expect(chain).toHaveAccessibleName(/state-undetermined.*\\xrightarrow\[\?\].*state-zero.*\\xrightarrow\[0\]/);
});
