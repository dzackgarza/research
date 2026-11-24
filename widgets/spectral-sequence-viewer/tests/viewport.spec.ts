import { expect, test } from "@playwright/test";

test("fit, zoom, pan and reset a square lattice",async({page})=>{
  await page.goto("/examples/static/");
  const figure=page.locator("spectral-sequence-viewer");
  const data={convention:"cohomological",firstPage:2,extent:{pMin:0,pMax:20,qMin:0,qMax:20},pages:[{index:2,terms:[{p:4,q:6,status:"nonzero"},{p:6,q:5,status:"nonzero"}],maps:[]}]};
  await figure.evaluate((el,d)=>{Object.assign(el,{sequence:d})},data);
  const chart=figure.getByRole("group",{name:"Chart viewport"});
  await expect(chart).toBeVisible();
  const bounds=await chart.boundingBox();
  expect(Math.abs(bounds!.width-bounds!.height)).toBeLessThan(2);
  const cells=figure.locator(".cell");
  await expect(cells).toHaveCount(9);
  const center={x:bounds!.x+bounds!.width/2,y:bounds!.y+bounds!.height/2};
  await page.mouse.move(center.x,center.y);
  await page.mouse.wheel(0,400);
  await expect.poll(()=>cells.count()).toBeGreaterThan(9);
  await figure.getByRole("button",{name:"Reset view"}).click();
  const first=await cells.first().getAttribute("aria-label");
  await page.mouse.move(center.x,center.y);await page.mouse.down();
  await page.mouse.move(center.x+bounds!.width*.4,center.y,{steps:5});await page.mouse.up();
  await expect(cells.first()).not.toHaveAttribute("aria-label",first!);
  await figure.getByRole("button",{name:"Reset view"}).click();
  await expect(cells.first()).toHaveAttribute("aria-label",first!);
});
