import Ajv from "ajv";
import schema from "../schema/sequence.schema.json";
import {
  endpoint,
  forcedZero,
  inside,
  outsideSupport,
  termStatus,
} from "./differentials";

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
export interface ChartClass {
  id: string;
  label: string;
  permanent?: boolean;
  previous?: string;
}
export interface Relation {
  kind: "multiplication" | "extension";
  source: string;
  target: string;
  formula: string;
}
export interface Term extends Point {
  status: "zero" | "nonzero" | "unknown";
  label?: string;
  generator?: string;
  module?: string;
  classes?: ChartClass[];
}
export interface Arrow extends Point {
  assignments?: {
    generator: string;
    image: string;
    sourceClass?: string;
    targetClass?: string;
  }[];
  image?: string;
  status: "zero" | "nonzero" | "undetermined";
  formula?: string;
}
export interface Page {
  index: number;
  terms: Term[];
  maps: Arrow[];
  relations?: Relation[];
  formula?: string;
}
export interface Sequence {
  support?: "unrestricted" | "first-quadrant";
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
    projection?: "native" | "total-filtration";
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
  const stableStatuses = new Map<string, "zero" | "nonzero">();
  // Only an explicitly listed coordinate can differ from the common unlisted policy.
  const termPoints = new Map(
    data.pages.flatMap((page) => page.terms.map((t) => [key(t), t] as const)),
  );
  const range = viewport(data);
  const coordinate = (point: Point, field: string) => {
    if (!Number.isSafeInteger(point.p) || !Number.isSafeInteger(point.q))
      fail(field + " exceeds the safe integer coordinate range");
    return point;
  };
  const inspectable = new Map<string, Point>();
  for (const p of [range.pMin, range.pMax])
    for (const q of [range.qMin, range.qMax]) {
      // Both projections and both differential displacements are affine.
      const corner = coordinate({ p, q }, "projected extent");
      const native = coordinate(nativePoint(data, corner), "inverse viewport");
      inspectable.set(key(native), native);
    }
  // An authored arrow or relation may select a source outside the viewport.
  // The viewer keeps that coordinate when the reader changes pages.
  for (const page of data.pages)
    for (const point of [...page.maps, ...page.terms])
      inspectable.set(key(point), point);
  data.pages.forEach((page, i) => {
    if (page.index !== data.firstPage + i)
      fail("pages[" + i + "].index expected " + (data.firstPage + i));
    unique(page.terms, "page " + page.index + " terms");
    unique(page.maps, "page " + page.index + " maps");
    const model = indexPage(data, page);
    for (const point of inspectable.values()) {
      const field = "page " + page.index + " coordinate " + key(point);
      coordinate(plotPoint(data, point), field);
      for (const direction of [-1, 1] as const) {
        const end = coordinate(endpoint(model, point, direction), field);
        coordinate(plotPoint(data, end), field);
      }
    }
    for (const [coord, point] of termPoints) {
      if (
        page.index <
        Math.min(
          data.degenerationPage ?? Infinity,
          model.stable.get(coord) ?? Infinity,
        )
      )
        continue;
      const status = termStatus(model, point);
      if (status === "unknown") continue;
      const previous = stableStatuses.get(coord);
      if (previous && previous !== status)
        fail(
          `page ${page.index} terms ${coord}: stable term changed from ${previous} to ${status}`,
        );
      stableStatuses.set(coord, status);
    }
    for (const term of page.terms) {
      for (const c of term.classes ?? []) {
        if (term.status !== "nonzero")
          fail(
            `page ${page.index} terms ${key(term)}: ` +
              "classes require a nonzero term",
          );
        if (
          c.previous &&
          !data.pages[i - 1]?.terms
            .find((t) => key(t) === key(term))
            ?.classes?.some((old) => old.id === c.previous)
        )
          fail(
            `page ${page.index} terms ${key(term)}: ` +
              "invalid previous class " +
              c.previous,
          );
      }
    }
    for (const [j, relation] of (page.relations ?? []).entries()) {
      const field = `page ${page.index} relations[${j}]`;
      for (const side of ["source", "target"] as const)
        if (!model.classes.has(relation[side]))
          fail(`${field}.${side}: unknown class ${relation[side]}`);
      if (relation.kind === "extension" && page.index !== data.degenerationPage)
        fail(field + ".kind: extensions require the limiting page");
    }
    for (const term of page.terms)
      if (term.status !== "zero" && outsideSupport(data, term))
        fail(
          "page " +
            page.index +
            " terms " +
            key(term) +
            " outside declared support",
        );
    for (const map of page.maps) {
      const zero =
        map.status === "zero" ||
        forcedZero(model, map, endpoint(model, map, 1));
      for (const [i, assignment] of (map.assignments ?? []).entries()) {
        for (const [id, point] of [
          [assignment.sourceClass, map],
          [assignment.targetClass, endpoint(model, map, 1)],
        ] as const) {
          if (id && model.classes.get(id)?.term !== model.terms.get(key(point)))
            fail(
              `page ${page.index} maps ${key(map)}: ` +
                "incorrect class endpoint " +
                id,
            );
          if (id && !model.classes.has(id))
            fail(
              `page ${page.index} maps ${key(map)}: ` + "unknown class " + id,
            );
        }
        const target =
          assignment.targetClass && model.classes.get(assignment.targetClass);
        if (zero && target && assignment.image.trim() === target.c.label.trim())
          fail(
            `page ${page.index} maps ${key(map)} assignments[${i}]: a zero differential cannot have image ${target.c.label}`,
          );
        if (
          assignment.sourceClass &&
          model.classes.get(assignment.sourceClass)?.c.permanent &&
          assignment.image.trim() !== "0"
        )
          fail(
            `page ${page.index} maps ${key(map)}: ` +
              "permanent class has nonzero image",
          );
      }
      const generators =
        map.assignments?.map((assignment) => assignment.generator) ?? [];
      if (new Set(generators).size !== generators.length)
        fail(
          "page " +
            page.index +
            " maps " +
            key(map) +
            " has duplicate generator assignments",
        );
    }
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
  const classes = new Map<string, { c: ChartClass; term: Term }>();
  for (const term of page.terms)
    for (const c of term.classes ?? []) {
      if (classes.has(c.id))
        throw new Error(
          `page ${page.index} terms ${key(term)}: ` + "duplicate class " + c.id,
        );
      classes.set(c.id, { c, term });
    }
  return {
    classes,
    data,
    page,
    terms: new Map(page.terms.map((t) => [key(t), t])),
    maps: new Map(page.maps.map((m) => [key(m), m])),
    stable: new Map(data.stableTerms?.map((t) => [key(t), t.fromPage])),
  };
}
export type Model = ReturnType<typeof indexPage>;

export function plotPoint(data: Sequence, point: Point): Point {
  return data.settings?.projection === "total-filtration"
    ? { p: point.p + point.q, q: point.p }
    : point;
}

export function nativePoint(data: Sequence, point: Point): Point {
  return data.settings?.projection === "total-filtration"
    ? { p: point.q, q: point.p - point.q }
    : point;
}

export function viewport(data: Sequence): Rect {
  if (data.settings?.viewport) return data.settings.viewport;
  const { pMin, pMax, qMin, qMax } = data.extent;
  const lo = plotPoint(data, { p: pMin, q: qMin });
  const hi = plotPoint(data, { p: pMax, q: qMax });
  return { pMin: lo.p, pMax: hi.p, qMin: lo.q, qMax: hi.q };
}
