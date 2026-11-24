import { test, expect } from "@playwright/test";
test("local permanence has a first page independent of global degeneration", async ({
  page,
}) => {
  await page.goto("/examples/static/");
  const cell = page.getByRole("button", { name: "(0,0)", exact: true });
  const pages = page.getByLabel("Page", { exact: true });
  await pages.selectOption("1");
  const before = await cell.evaluate(
    (el) => getComputedStyle(el).backgroundColor,
  );
  await expect(cell).not.toContainText("stable");
  await pages.selectOption("2");
  await expect(cell).toContainText("stable");
  expect(
    await cell.evaluate((el) => getComputedStyle(el).backgroundColor),
  ).not.toBe(before);
  await cell.click();
  const inspector = page.getByRole("region", { name: "Inspector" });
  await expect(inspector).toContainText("stable from page 2");
  await expect(inspector.getByRole("img")).toHaveAccessibleName(
    /E_2\^\{-2,1\}.*\\xrightarrow\[\]\{0\}.*E_2\^\{0,0\}.*\\xrightarrow\[\]\{0\}.*E_2\^\{2,-1\}/,
  );
  await pages.selectOption("3");
  await expect(inspector).toContainText("stable from page 2");
  await expect(
    page.getByRole("button", { name: "(1,1)", exact: true }),
  ).not.toContainText("stable");
});
