import { expect, test } from "@playwright/test";

test("the Serre article typesets its title, captions and conclusion", async ({ page }) => {
  await page.goto("/examples/serre/");
  for (const selector of ["h1", "figcaption", "main > p:last-of-type"]) {
    await expect(page.locator(selector).first().locator("mjx-container svg").first()).toBeVisible({timeout: 2500});
  }
});
