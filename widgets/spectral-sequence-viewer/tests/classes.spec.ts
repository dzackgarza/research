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

test("zero component rejects an assignment to the target class itself", async ({
  page,
}) => {
  await page.goto("/examples/static/");
  const figure = page.locator("spectral-sequence-viewer");
  for (const forced of [false, true]) {
    const data = structuredClone(shared);
    if (forced) data.degenerationPage = 2;
    data.pages[0].maps[0].status = forced ? "undetermined" : "zero";
    data.pages[0].maps[0].assignments[0].image = "z";
    await expect(
      figure.evaluate((el, d) => {
        Object.assign(el, { sequence: d });
      }, data),
    ).rejects.toThrow(/page 2.*assignments\[0\]/);
    await expect(figure.getByLabel("Page", { exact: true })).toHaveValue("2");
  }
});

test("mixed assignments retain an unnamed nonzero image on the plot", async ({
  page,
}) => {
  const data = structuredClone(shared);
  data.pages[0].maps[0].assignments = [
    { generator: "x", image: "2z" },
    { generator: "y", image: "0", sourceClass: "y", targetClass: "z" },
  ] as (typeof data.pages)[0]["maps"][0]["assignments"];
  await page.goto("/examples/static/");
  const figure = page.locator("spectral-sequence-viewer");
  await figure.evaluate((el, d) => {
    Object.assign(el, { sequence: d });
  }, data);
  await figure.getByRole("button", { name: "Display options" }).click();
  await figure.getByLabel("Arrows").selectOption("Known nonzero");
  await expect(
    figure.getByRole("button", {
      name: "Differential (0,1) to (2,0)",
      exact: true,
    }),
  ).toBeVisible();
});

test("class selection highlights only incident named edges", async ({
  page,
}) => {
  await page.goto("/examples/static/");
  const figure = page.locator("spectral-sequence-viewer");
  await figure.evaluate((el, d) => {
    Object.assign(el, { sequence: d });
  }, shared);
  await figure.getByRole("button", { name: "Class y", exact: true }).click();
  await expect(
    figure.locator('line[data-status="nonzero"][data-highlighted="true"]'),
  ).toHaveCount(0);
  await figure.getByRole("button", { name: "Class x", exact: true }).click();
  await expect(
    figure.locator('line[data-status="nonzero"][data-highlighted="true"]'),
  ).toHaveCount(1);
});

test("term stability is visible on the chart with named classes", async ({
  page,
}) => {
  await page.goto("/examples/static/");
  const figure = page.locator("spectral-sequence-viewer");
  await figure.evaluate(
    (el, d) => {
      Object.assign(el, { sequence: d });
    },
    { ...shared, stableTerms: [{ ...a, fromPage: 3 }] },
  );
  await expect(
    figure.locator(".plot").getByText("stable", { exact: true }),
  ).toHaveCount(0);
  await figure.getByRole("button", { name: "Next" }).click();
  await expect(
    figure.locator(".plot").getByText("stable", { exact: true }),
  ).toBeVisible();
});

test("parallel products can each be selected by pointer and keyboard", async ({
  page,
}) => {
  const data = structuredClone(shared);
  const relations = data.pages[0].relations!;
  relations.push({ ...relations[0], formula: "kx=z" });
  await page.goto("/examples/static/");
  const figure = page.locator("spectral-sequence-viewer");
  await figure.evaluate((el, d) => {
    Object.assign(el, { sequence: d });
  }, data);
  for (const relation of relations) {
    const edge = figure.getByRole("button", {
      name: "Multiplication x to z " + relation.formula,
      exact: true,
    });
    await edge.press("Enter");
    await expect(
      figure.getByLabel(relation.formula, { exact: true }),
    ).toBeVisible();
    const pos = await edge.evaluate((el) => {
      const path = el as SVGPathElement;
      const point = path
        .getPointAtLength(path.getTotalLength() / 2)
        .matrixTransform(path.getScreenCTM()!);
      return { x: point.x, y: point.y };
    });
    await figure.getByRole("button", { name: "Class x", exact: true }).click();
    await page.mouse.click(pos.x, pos.y);
    await expect(
      figure.getByLabel(relation.formula, { exact: true }),
    ).toBeVisible();
  }
});
