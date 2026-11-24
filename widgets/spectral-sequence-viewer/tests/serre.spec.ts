import { expect, test } from "@playwright/test";

test("the Serre article typesets its title, captions and conclusion", async ({ page }) => {
  await page.goto("/examples/serre/");
  for (const selector of ["h1", "figcaption", "main > p:last-of-type"]) {
    await expect(page.locator(selector).first().locator("mjx-container svg").first()).toBeVisible({timeout: 2500});
  }
});

test("the transgression identifies the modules and sends each generator to its image", async ({ page }) => {
  await page.goto("/examples/serre/");
  const figure = page.locator("#co");
  await figure.getByRole("button", { name: "(3,2)", exact: true }).click();
  const chain = figure.locator(".chain > svg");
  await expect(chain.locator('[data-mml-node="mtr"]')).toHaveCount(3);
  await expect(chain).toHaveAccessibleName(/d_3\^\{0,4\}.*d_3\^\{3,2\}.*state-zero.*E_3\^\{6,0\}/);
  await expect(chain).toHaveAccessibleName(/x\^\{2\}.*\\mapsto 2ux.*ux.*\\mapsto 0/);
});
