import { test, expect } from "@playwright/test";
import sequence from "../examples/sequence.json" with { type: "json" };
test("inspect clipped maps through all filters and zero styles", async ({
  page,
}) => {
  await page.goto("/examples/static/");
  await page.getByRole("button", { name: "(2,1)", exact: true }).click();
  const inspector = page.getByRole("region", { name: "Inspector" });
  for (const [index, pair] of ["(0,2)", "(2,1)", "(2,1)", "(4,0)"].entries()) {
    const endpoint = inspector
      .locator("p mjx-container svg[aria-label]")
      .nth(index);
    await expect(endpoint).toHaveAttribute("aria-label", pair, {
      timeout: 2500,
    });
    await expect(endpoint).toBeVisible();
  }
  await page.getByText("Display options", { exact: true }).click();
  for (const mode of ["All", "Potentially nonzero", "Known nonzero", "None"]) {
    await page.getByLabel("Arrows").selectOption(mode);
    await expect(
      inspector
        .locator("span")
        .filter({ has: page.getByRole("img", { name: "(0,2)", exact: true }) }),
    ).toHaveText("offscreen");
    await expect(
      inspector.getByRole("img", { name: "(4,0)", exact: true }),
    ).toBeVisible();
    await expect(inspector).toContainText("undetermined");
    await expect(inspector.locator("svg")).not.toHaveCount(0);
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
    await page.getByLabel("Zero style").selectOption(style);
    const zero = page.getByRole("button", { name: "(1,0)", exact: true });
    await zero.focus();
    await zero.press("Enter");
    await expect(inspector).toContainText("zero");
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
  await expect(
    inspector
      .locator("p")
      .filter({ hasText: "Incoming" })
      .getByRole("img", { name: "(4,0)", exact: true }),
  ).toBeVisible();
  const outgoing = inspector.locator("p").filter({ hasText: "Outgoing" });
  await expect(
    outgoing.getByRole("img", { name: "(2,1)", exact: true }),
  ).toBeVisible();
  await expect(
    outgoing
      .locator("span")
      .filter({ has: page.getByRole("img", { name: "(0,2)", exact: true }) }),
  ).toHaveText("offscreen");
});
