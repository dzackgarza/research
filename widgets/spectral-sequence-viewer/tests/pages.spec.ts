import { test, expect } from "@playwright/test";
import sequence from "../examples/sequence.json" with { type: "json" };
test("navigate pages with the keyboard and retain the selected coordinate", async ({
  page,
}) => {
  await page.goto("/examples/static/");
  await page.getByRole("button", { name: "(2,1)", exact: true }).click();
  const selector = page.getByLabel("Page", { exact: true });
  await page.getByRole("button", { name: "Next" }).press("Enter");
  await expect(selector).toHaveValue("3");
  await expect(selector.locator("option:checked")).toHaveText("E₃ = E∞");
  await expect(page.getByRole("button", { name: "Next" })).toBeDisabled();
  await expect(page.getByRole("region", { name: "Inspector" })).toContainText(
    "(2,1)",
  );
  await expect(page.getByLabel("Page formula").locator("svg")).toBeVisible();
  await page.getByRole("button", { name: "Previous" }).press("Enter");
  await expect(selector).toHaveValue("2");
  await selector.press("Home");
  await expect(page.getByRole("button", { name: "Previous" })).toBeDisabled();
  for (const degenerationPage of [2, 7, undefined]) {
    const data = { ...sequence, degenerationPage };
    if (degenerationPage === 2)
      data.pages = sequence.pages.map((p) => ({ ...p, maps: [] }));
    await page
      .locator("spectral-sequence-viewer")
      .evaluate((el, d) => Object.assign(el, { sequence: d }), data);
    await expect(selector.locator("option")).toHaveCount(4);
    await expect(
      selector.locator("option").filter({ hasText: "∞" }),
    ).toHaveCount(degenerationPage === 2 ? 1 : 0);
  }
});
