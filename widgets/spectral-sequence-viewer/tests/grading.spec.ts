import { test, expect } from "@playwright/test";

for (const convention of ["cohomological", "homological"]) {
  test(convention + " component in native and total degree", async ({ page }) => {
    await page.goto("/examples/static/");
    const viewer = page.locator("spectral-sequence-viewer");
    const a = { p: -2, q: 3 }, b = { p: 0, q: 2 };
    const [source, target] = convention === "cohomological" ? [a, b] : [b, a];
    for (const projection of ["native", "total-filtration"]) {
      const data = {
        convention, firstPage: 2, support: "unrestricted",
        extent: { pMin: -2, pMax: 0, qMin: 2, qMax: 3 },
        settings: { projection },
        pages: [{ index: 2, terms: [
          { ...source, status: "nonzero", module: "A" },
          { ...target, status: "nonzero", module: "B" },
        ], maps: [{ ...source, status: "nonzero", assignments: [
          { generator: "a", image: "u" }, { generator: "b", image: "0" },
        ] }] }],
      };
      await viewer.evaluate((el, input) => { Object.assign(el, { sequence: input }); }, data);
      const cell = viewer.getByRole("button", { name: "(-2,3)", exact: true });
      await cell.click();
      await expect(viewer.locator(".chain > svg")).toHaveAccessibleName(/&*a&.*longmapsto.*&u.*b&.*longmapsto.*&0/);
      await expect(viewer.locator('line[data-status="nonzero"]')).toHaveCount(1);
      await cell.press("ArrowRight");
      const next = projection === "native" ? "(-1,3)" : "(-2,4)";
      await expect(viewer.getByRole("button", { name: next, exact: true })).toHaveAttribute("data-status", "unknown");
      await expect(viewer.getByRole("button", { name: next, exact: true })).toBeFocused();
    }
  });
}
