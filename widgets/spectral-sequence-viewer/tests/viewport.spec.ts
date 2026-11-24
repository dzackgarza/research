import { expect, test } from "@playwright/test";

test("fit, zoom, pan and reset a square lattice", async ({ page }) => {
  await page.goto("/examples/static/");
  const figure = page.locator("spectral-sequence-viewer");
  const data = {
    convention: "cohomological",
    firstPage: 2,
    extent: { pMin: 0, pMax: 20, qMin: 0, qMax: 20 },
    pages: [
      {
        index: 2,
        terms: [
          { p: 4, q: 6, status: "nonzero" },
          { p: 6, q: 5, status: "nonzero" },
        ],
        maps: [],
      },
    ],
  };
  await figure.evaluate((el, d) => {
    Object.assign(el, { sequence: d });
  }, data);
  const chart = figure.getByRole("group", { name: "Chart viewport" });
  await expect(chart).toBeVisible();
  const bounds = await chart.boundingBox();
  expect(Math.abs(bounds!.width - bounds!.height)).toBeLessThan(2);
  const cells = figure.locator(".cell");
  await expect(cells).toHaveCount(9);
  const at = (name: string) =>
    figure.getByRole("button", { name, exact: true }).boundingBox();
  const origin = await at("(4,5)"),
    right = await at("(5,5)"),
    above = await at("(4,6)");
  expect(right!.x - origin!.x).toBeCloseTo(origin!.y - above!.y, 0);
  const center = {
    x: bounds!.x + bounds!.width / 2,
    y: bounds!.y + bounds!.height / 2,
  };
  await page.mouse.move(center.x, center.y);
  await page.mouse.wheel(0, 100);
  await expect.poll(() => cells.count()).toBeGreaterThan(9);
  await figure.getByRole("button", { name: "Reset view" }).click();
  const first = await cells.first().getAttribute("aria-label");
  await page.mouse.move(center.x, center.y);
  await page.mouse.down();
  await page.mouse.move(center.x + bounds!.width * 0.4, center.y, { steps: 5 });
  await page.mouse.up();
  await expect(cells.first()).not.toHaveAttribute("aria-label", first!);
  await figure.getByRole("button", { name: "Reset view" }).click();
  await expect(cells.first()).toHaveAttribute("aria-label", first!);
});

test("swipe and pinch on a phone preserve the inspected term", async ({
  browser,
}) => {
  const context = await browser.newContext({
    viewport: { width: 375, height: 760 },
    hasTouch: true,
    isMobile: true,
  });
  try {
    const page = await context.newPage();
    await page.goto("http://127.0.0.1:4180/examples/serre/");
    const figure = page.locator("spectral-sequence-viewer").first();
    const chart = figure.getByRole("group", { name: "Chart viewport" });
    await chart.scrollIntoViewIfNeeded();
    const bounds = (await chart.boundingBox())!;
    expect(Math.abs(bounds.width - bounds.height)).toBeLessThan(2);
    const x = bounds.x + bounds.width / 2,
      y = bounds.y + bounds.height / 2;
    const cells = figure.locator(".cell");
    const first = await cells.first().getAttribute("aria-label");
    const chain = figure.locator(".chain > svg");
    const terms = () =>
      chain
        .getAttribute("aria-label")
        .then((tex) => tex?.match(/E_\d+\^\{[-\d,]+\}/g));
    const selected = await terms();
    const session = await context.newCDPSession(page);
    const touch = (
      type: "touchStart" | "touchMove" | "touchEnd",
      xs: number[],
    ) =>
      session.send("Input.dispatchTouchEvent", {
        type,
        touchPoints: xs.map((x, id) => ({ x, y, id: id + 1 })),
      });
    await touch("touchStart", [x]);
    await touch("touchMove", [x + bounds.width * 0.3]);
    await touch("touchEnd", []);
    await expect(cells.first()).not.toHaveAttribute("aria-label", first!);
    const before = await cells.count();
    await touch("touchStart", [x - 25, x + 25]);
    await touch("touchMove", [x - 55, x + 55]);
    await touch("touchEnd", []);
    await expect.poll(() => cells.count()).toBeLessThan(before);
    expect(await terms()).toEqual(selected);
    await figure.getByRole("button", { name: "Reset view" }).click();
    await expect(cells.first()).toHaveAttribute("aria-label", first!);
  } finally {
    await context.close();
  }
});

test("a sparse overview fits a distant nonzero differential and inspects empty boxes", async ({
  page,
}) => {
  await page.goto("/examples/static/");
  const figure = page.locator("spectral-sequence-viewer");
  const data = {
    firstPage: 100,
    convention: "cohomological",
    extent: { pMin: 0, pMax: 1000, qMin: 0, qMax: 1000 },
    pages: [
      {
        index: 100,
        terms: [{ p: 10, q: 99, status: "nonzero" }],
        maps: [{ p: 10, q: 99, status: "nonzero" }],
      },
    ],
  };
  await figure.evaluate((el, d) => {
    Object.assign(el, { sequence: d });
  }, data);
  const chart = figure.getByRole("group", { name: "Chart viewport" });
  await expect(
    figure.getByRole("button", { name: "Differential (10,99) to (110,0)" }),
  ).toBeVisible();
  await chart.scrollIntoViewIfNeeded();
  const b = (await chart.boundingBox())!;
  await page.mouse.click(b.x + b.width * 0.25, b.y + b.height * 0.2);
  await expect(
    figure.getByRole("button", { name: "(35,80)", exact: true }),
  ).toHaveAttribute("aria-pressed", "true");
});
