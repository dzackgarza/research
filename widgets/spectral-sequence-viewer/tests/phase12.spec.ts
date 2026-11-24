import { expect, test } from "@playwright/test";

const point = {p:0,q:0};
const extent = {pMin:0,pMax:0,qMin:0,qMax:0};
const base = {convention:"cohomological",firstPage:2,extent};

test("stable term assertions agree across supplied pages",async({page})=>{
  await page.goto("/examples/static/");
  const figure=page.locator("spectral-sequence-viewer");
  for (const stability of [{stableTerms:[{...point,fromPage:2}]},{degenerationPage:2}]) {
    const pages=["nonzero","unknown","nonzero"].map((status,i)=>({index:2+i,terms:[{...point,status}],maps:[]}));
    const data={...base,...stability,pages,unlisted:"zero"};
    await figure.evaluate((el,d)=>{Object.assign(el,{sequence:d})},data);
    pages[2].terms=[];
    await expect(figure.evaluate((el,d)=>{Object.assign(el,{sequence:d})},data)).rejects.toThrow(/page 4.*0,0/);
    await expect(figure.getByLabel("Page",{exact:true})).toHaveValue("2");
  }
});

test("representable input must have representable chart and incident coordinates",async({page})=>{
  await page.goto("/examples/static/");
  const figure=page.locator("spectral-sequence-viewer");
  await expect(figure.getByLabel("Page",{exact:true})).toHaveValue("2");
  const session=await page.context().newCDPSession(page);
  const max=Number.MAX_SAFE_INTEGER;
  const single=(p:number,q:number)=>({pMin:p,pMax:p,qMin:q,qMax:q});
  for(const chart of [
    {extent:single(max,0)},
    {settings:{projection:"total-filtration",viewport:single(max,-1)}},
    {extent:single(max,1),settings:{projection:"total-filtration"}},
  ]){
    const data={...base,...chart,pages:[{index:2,terms:[],maps:[]}]};
    // Bound evaluation externally: unsafe tick increments can stall the renderer.
    const result=await session.send("Runtime.evaluate",{expression:
      'document.querySelector("spectral-sequence-viewer").sequence='+JSON.stringify(data),timeout:1500});
    expect(result.exceptionDetails?.exception?.description).toMatch(/(viewport|extent|page 2).*safe integer/i);
    await expect(figure.getByLabel("Page",{exact:true})).toHaveValue("2");
  }
});

test("inspect a named class with both a term label and a module",async({page})=>{
  await page.goto("/examples/static/");
  const figure=page.locator("spectral-sequence-viewer");
  await figure.evaluate((el,d)=>{Object.assign(el,{sequence:d})},{...base,pages:[{index:2,maps:[],terms:[{...point,status:"nonzero",label:"L",module:"M",classes:[{id:"x",label:"x"}]}]}]});
  await figure.getByRole("button",{name:"Class x"}).click();
  const panel=figure.getByRole("region",{name:"Inspector"});
  for(const code of ["1D43F","1D440","1D465"]) await expect(panel.locator('svg [data-c="'+code+'"]').first()).toBeVisible();
});
