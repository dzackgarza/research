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

test("generator images occupy the column of their receiving module", async ({ page }) => {
  await page.goto("/examples/serre/");
  const figure = page.locator("#co");
  await figure.getByRole("button", { name: "(3,2)", exact: true }).click();
  const rows = figure.locator('.chain [data-mml-node="mtr"]');
  for (const [row, col] of [[2, 2], [3, 4]]) {
    const center = async (r: number) => rows.nth(r).locator('[data-mml-node="mtd"]').nth(col)
      .evaluate(el => { const b = el.getBoundingClientRect(); return { x: b.x + b.width / 2, width: b.width }; });
    const module = await center(1);
    const image = await center(row);
    expect(image.width).toBeGreaterThan(0);
    expect(Math.abs(module.x - image.x)).toBeLessThan(2);
  }
});
