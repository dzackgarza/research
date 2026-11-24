import Ajv from "ajv";
import schema from "../schema/sequence.schema.json";
import { endpoint, forcedZero, inside } from "./differentials";

export interface Point {
  p: number;
  q: number;
}
export interface Rect {
  pMin: number;
  pMax: number;
  qMin: number;
  qMax: number;
}
export interface Term extends Point {
  status: "zero" | "nonzero" | "unknown";
  label?: string;
  generator?: string;
  module?: string;
}
export interface Arrow extends Point {
  image?: string;
  status: "zero" | "nonzero" | "undetermined";
  formula?: string;
}
export interface Page {
  index: number;
  terms: Term[];
  maps: Arrow[];
  formula?: string;
}
export interface Sequence {
  supportedColumns?: number[];
  firstPage: number;
  pages: Page[];
  convention: "cohomological" | "homological";
  extent: Rect;
  unlisted?: "zero" | "unknown";
  pageCount?: number;
  degenerationPage?: number;
  stableTerms?: (Point & { fromPage: number })[];
  settings?: {
    viewport?: Rect;
    initialPage?: number;
    title?: string;
    pLabel?: string;
    qLabel?: string;
    zeroStyle?: "zero" | "dot" | "blank";
  };
}
export const key = ({ p, q }: Point) => p + "," + q;
const validate = new Ajv().compile<Sequence>(schema);
export function parseSequence(input: Sequence): Sequence {
  if (!validate(input)) throw new Error(new Ajv().errorsText(validate.errors));
  const data = structuredClone(input);
  const fail = (message: string): never => {
    throw new Error(message);
  };
  for (const [name, r] of [
    ["extent", data.extent],
    ["settings.viewport", data.settings?.viewport],
  ] as const)
    if (r && (r.pMin > r.pMax || r.qMin > r.qMax))
      fail(name + " has reversed bounds");
  if (data.pageCount !== undefined && data.pageCount !== data.pages.length)
    fail("pageCount differs from pages.length");
  if (
    data.settings?.initialPage !== undefined &&
    !data.pages.some((p) => p.index === data.settings!.initialPage)
  )
    fail("settings.initialPage is outside supplied pages");
  const unique = (points: Point[], field: string) => {
    const seen = new Set<string>();
    for (const point of points) {
      const coord = key(point);
      if (seen.has(coord)) fail(field + " duplicate " + coord);
      if (!inside(point, data.extent)) fail(field + " outside extent " + coord);
      seen.add(coord);
    }
  };
  unique(data.stableTerms ?? [], "stableTerms");
  data.pages.forEach((page, i) => {
    if (page.index !== data.firstPage + i)
      fail("pages[" + i + "].index expected " + (data.firstPage + i));
    unique(page.terms, "page " + page.index + " terms");
    unique(page.maps, "page " + page.index + " maps");
    const model = indexPage(data, page);
    for (const arrow of page.maps)
      if (
        arrow.status === "nonzero" &&
        forcedZero(model, arrow, endpoint(model, arrow, 1))
      )
        fail(
          "page " +
            page.index +
            " maps " +
            key(arrow) +
            " conflicts with forced zero",
        );
  });
  return data;
}
export function indexPage(data: Sequence, page: Page) {
  return {
    data,
    page,
    terms: new Map(page.terms.map((t) => [key(t), t])),
    maps: new Map(page.maps.map((m) => [key(m), m])),
    stable: new Map(data.stableTerms?.map((t) => [key(t), t.fromPage])),
  };
}
export type Model = ReturnType<typeof indexPage>;
