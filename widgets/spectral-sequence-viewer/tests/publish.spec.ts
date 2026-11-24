import { test, expect } from "@playwright/test";
import fixture from "../examples/sequence.json" with { type: "json" };
test("articles and late insertion publish independent figures", async ({
  page,
}) => {
  for (const url of [
    "/examples/static/",
    "http://127.0.0.1:4181/examples/react/",
  ]) {
    await page.goto(url);
    await expect(page.getByLabel("Page", { exact: true })).toHaveValue("2");
    await expect(page.getByRole("heading").locator("svg")).toBeVisible();
  }
  await page.goto("/examples/static/");
  await page.getByText("Insert figure").click();
  const selectors = page.getByLabel("Page", { exact: true });
  await selectors.nth(1).selectOption("1");
  await expect(selectors.first()).toHaveValue("2");
});
test("rejects invalid replacements atomically", async ({ page }) => {
  await page.goto("/examples/static/");
  await expect(page.getByLabel("Page", { exact: true })).toHaveValue("2");
  for (const [field, change] of [
    ["pageCount", (d) => d.pageCount++],
    ["index", (d) => (d.pages[1].index = 8)],
    ["duplicate", (d) => d.pages[2].terms.push(d.pages[2].terms[0])],
    ["terms", (d) => (d.pages[0].terms[0].p = -1)],
    [
      "2 maps",
      (d) => (d.pages[2].terms.find((t) => t.label === "A")!.status = "zero"),
    ],
    ["2 maps", (d) => (d.degenerationPage = 2)],
  ] as [string, (d: typeof fixture) => void][]) {
    const data = structuredClone(fixture);
    change(data);
    await expect(
      page
        .locator("spectral-sequence-viewer")
        .evaluate((el, d) => Object.assign(el, { sequence: d }), data),
    ).rejects.toThrow(field);
    await expect(page.getByLabel("Page", { exact: true })).toHaveValue("2");
  }
});
