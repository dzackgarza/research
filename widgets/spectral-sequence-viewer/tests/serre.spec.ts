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
  await expect(chain.locator('[data-mml-node="mtr"]')).toHaveCount(4);
  await expect(chain).toHaveAccessibleName(/d_3\^\{0,4\}.*d_3\^\{3,2\}.*state-zero.*E_3\^\{6,0\}/);
  await expect(chain).toHaveAccessibleName(/x\^\{2\}.*\\longmapsto.*2ux.*ux.*\\longmapsto.*0/);
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

test("display options leave the figure caption in place", async ({ page }) => {
  await page.goto("/examples/serre/");
  const figure = page.locator("figure").first();
  const options = figure.getByText("Display options", { exact: true });
  await options.scrollIntoViewIfNeeded();
  const caption = figure.locator("figcaption");
  const position = () => caption.evaluate(el => el.getBoundingClientRect().top + scrollY);
  const before = await position();
  await options.click();
  await expect(figure.getByLabel("Arrows")).toBeVisible();
  expect(await position()).toBeCloseTo(before, 0);
  await figure.getByLabel("Arrows").selectOption("None");
  await expect(figure.locator("line[data-status]")).toHaveCount(0);
  await figure.getByLabel("Arrows").press("Escape");
  await expect(figure.getByLabel("Arrows")).toBeHidden();
});

test("the color key matches the plotted mathematical status", async ({ page }) => {
  await page.goto("/examples/serre/");
  const figure = page.locator("#co");
  await figure.getByRole("button", { name: "Color key" }).click();
  for (const status of ["zero", "nonzero"]) {
    const ink = await figure.locator(".guide .state-" + status).evaluate(el => getComputedStyle(el).color);
    await expect(figure.locator('.cell[data-status="' + status + '"]').first()).toHaveCSS("color", ink);
    await expect(figure.locator('line[data-status="' + status + '"]').first()).toHaveCSS("stroke", ink);
  }
});

test("Serre terms identify the integral module before and after passage to the quotient", async ({page}) => {
  await page.goto("/examples/serre/");
  for (const [id, degree, generator] of [["co","(3,2)","ux"],["ho","(0,4)","b_2"]]) {
    const figure=page.locator("#"+id);
    await figure.getByRole("button",{name:degree,exact:true}).click();
    const chain=figure.locator(".chain > svg");
    for (const [index,g,type] of [["2",generator,""],["3",generator,""],["4","["+generator+"]","/2"]]) {
      await figure.getByLabel("Page",{exact:true}).selectOption(index);
      expect(await chain.getAttribute("aria-label")).toContain("\\langle "+g+"\\rangle_{\\mathbb Z}\\cong\\mathbb Z"+type);
    }
  }
});
