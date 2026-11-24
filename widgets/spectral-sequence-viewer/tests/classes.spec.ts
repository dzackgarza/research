import { test, expect } from "@playwright/test";

const a = { p: 0, q: 1 },
  b = { p: 2, q: 0 };
const shared = {
  firstPage: 2,
  degenerationPage: 3,
  convention: "cohomological",
  extent: { pMin: 0, pMax: 2, qMin: 0, qMax: 1 },
  pages: [
    {
      index: 2,
      terms: [
        {
          ...a,
          status: "nonzero",
          classes: [
            { id: "x", label: "x" },
            { id: "y", label: "y", permanent: true },
          ],
        },
        { ...b, status: "nonzero", classes: [{ id: "z", label: "z" }] },
      ],
      maps: [
        {
          ...a,
          status: "nonzero",
          assignments: [
            { generator: "x", image: "2z", sourceClass: "x", targetClass: "z" },
          ],
        },
      ],
      relations: [
        { kind: "multiplication", source: "x", target: "z", formula: "hx=z" },
      ],
    },
    {
      index: 3,
      terms: [
        {
          ...a,
          status: "nonzero",
          classes: [{ id: "y", label: "y", previous: "y", permanent: true }],
        },
        {
          ...b,
          status: "nonzero",
          classes: [{ id: "residue", label: "[z]", previous: "z" }],
        },
      ],
      maps: [],
    },
  ],
};

test("inspect named classes, products and a quotient representative", async ({
  page,
}) => {
  await page.goto("/examples/static/");
  const figure = page.locator("spectral-sequence-viewer");
  await figure.evaluate((el, d) => {
    Object.assign(el, { sequence: d });
  }, shared);
  await expect(
    figure.getByRole("button", { name: "Class y", exact: true }),
  ).toContainText("permanent");
  await figure
    .getByRole("button", { name: "Differential x to z" })
    .press("Enter");
  await expect(figure.locator(".chain > svg")).toHaveAccessibleName(/2z/);
  await figure
    .getByRole("button", { name: "Multiplication x to z" })
    .press("Enter");
  await expect(figure.getByLabel("hx=z", { exact: true })).toBeVisible();
  await figure.getByRole("button", { name: "Class z", exact: true }).click();
  await figure.getByRole("button", { name: "Next", exact: true }).click();
  await expect(
    figure.getByRole("button", { name: "Class residue" }),
  ).toHaveAttribute("aria-pressed", "true");
  await expect(figure.getByRole("button", { name: /Extension/ })).toHaveCount(
    0,
  );
});

test("inspect an extension supplied on the limiting page", async ({ page }) => {
  await page.goto("/examples/static/");
  const figure = page.locator("spectral-sequence-viewer");
  const data = {
    ...shared,
    firstPage: 3,
    pages: [
      {
        index: 3,
        terms: [
          { p: 0, q: 1, status: "nonzero", classes: [{ id: "u", label: "u" }] },
          { p: 1, q: 0, status: "nonzero", classes: [{ id: "v", label: "v" }] },
        ],
        maps: [],
        relations: [
          {
            kind: "extension",
            source: "u",
            target: "v",
            formula: "0\\to C_2\\to C_4\\to C_2\\to0",
          },
        ],
      },
    ],
  };
  await figure.evaluate((el, d) => {
    Object.assign(el, { sequence: d });
  }, data);
  await figure.getByRole("button", { name: "Extension u to v" }).press("Enter");
  await expect(
    figure.getByLabel(data.pages[0].relations[0].formula, { exact: true }),
  ).toBeVisible();
});

test("inspect the segment with neither endpoint visible", async ({ page }) => {
  await page.goto("/examples/static/");
  const figure = page.locator("spectral-sequence-viewer");
  const data = {
    ...shared,
    settings: { viewport: { pMin: 1, pMax: 1, qMin: 0, qMax: 1 } },
  };
  await figure.evaluate((el, d) => {
    Object.assign(el, { sequence: d });
  }, data);
  await figure.getByRole("button", { name: "Differential x to z" }).click();
  await expect(figure.locator(".chain .clipped")).toHaveCount(3);
});

test("filter a zero generator image in a nonzero component", async ({
  page,
}) => {
  await page.goto("/examples/static/");
  const figure = page.locator("spectral-sequence-viewer");
  const data = structuredClone(shared);
  data.pages[0].maps[0].assignments.push({
    generator: "y",
    image: "0",
    sourceClass: "y",
    targetClass: "z",
  });
  await figure.evaluate((el, d) => {
    Object.assign(el, { sequence: d });
  }, data);
  const zero = figure.getByRole("button", { name: "Differential y to z" });
  await expect(zero).toBeVisible();
  await figure.getByRole("button", { name: "Display options" }).click();
  await figure.getByLabel("Arrows").selectOption("Known nonzero");
  await expect(zero).toHaveCount(0);
  await expect(
    figure.getByRole("button", { name: "Differential x to z" }),
  ).toBeVisible();
});

test("locate an invalid class reference in a relation", async ({ page }) => {
  await page.goto("/examples/static/");
  const data = structuredClone(shared);
  data.pages[0].relations![0].target = "absent";
  await expect(
    page.locator("spectral-sequence-viewer").evaluate((el, d) => {
      Object.assign(el, { sequence: d });
    }, data),
  ).rejects.toThrow(/page 2 relations\[0\].target.*absent/);
});

test("navigate between a named class and the adjacent grid cell", async ({
  page,
}) => {
  await page.goto("/examples/static/");
  const figure = page.locator("spectral-sequence-viewer");
  await figure.evaluate((el, d) => {
    Object.assign(el, { sequence: d });
  }, shared);
  await figure
    .getByRole("button", { name: "Class x", exact: true })
    .press("ArrowRight");
  const cell = figure.getByRole("button", { name: "(1,1)", exact: true });
  await expect(cell).toBeFocused();
  await cell.press("ArrowLeft");
  await expect(
    figure.getByRole("button", { name: "Class x", exact: true }),
  ).toBeFocused();
});
