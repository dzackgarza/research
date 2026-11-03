"""A21 dependency audit: every use of A21's labels in the corpus, mechanically extracted.

Scans the writing/ tree, docs/, TODO.md, HANDOFF.md for the labels under which A21 and its
chamber programme are stated, and separates the *definition* site of each label from its
*reference* sites (a reference is a downstream use).
"""
import os, re, json, subprocess, sys

ROOT = "/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo"
LABELS = [
 "prob:coble-rigidity", "prob:effective-cone-agreement", "thm:a21-labels",
 "prop:chamber-conditional", "prop:chamber-pinned", "lem:face-at-H",
 "rmk:a21-scope", "rmk:a21-open", "rmk:a21-resolution", "rmk:chamber-not-transported",
 "prob:twist-identification", "prob:projective-coverage", "prop:node-count-invariant",
 "cor:construction-monodromy", "prop:tuple-of-the-construction", "prop:one-node-family",
 "prop:one-node-connected", "thm:one-node-transport", "prop:del-pezzo-type-on-the-resolution",
 "prob:rank-one-geometry",
]
DIRS = ["writing", "docs"]
FILES = ["TODO.md", "HANDOFF.md", "INTENT.md"]

def sources():
    out = []
    for d in DIRS:
        for dp, _, fns in os.walk(os.path.join(ROOT, d)):
            if "/1.6/" in dp or "/archives/" in dp:
                continue
            for fn in fns:
                if fn.endswith(".md"):
                    out.append(os.path.join(dp, fn))
    for f in FILES:
        p = os.path.join(ROOT, f)
        if os.path.exists(p):
            out.append(p)
    return out

def main():
    rows = []
    for path in sources():
        try:
            lines = open(path, encoding="utf-8", errors="replace").read().split("\n")
        except OSError:
            continue
        for i, ln in enumerate(lines, 1):
            for lab in LABELS:
                # a definition site is a heading anchor {.kind #label ...}
                if re.search(r"\{\.\w+\s+#" + re.escape(lab) + r"\b", ln):
                    rows.append(dict(label=lab, file=os.path.relpath(path, ROOT), line=i,
                                     kind="DEFINITION", text=ln.strip()[:160]))
                for m in re.finditer(r"@" + re.escape(lab) + r"\b", ln):
                    # skip the definition site itself
                    if re.search(r"\{\.\w+\s+#" + re.escape(lab) + r"\b", ln):
                        continue
                    rows.append(dict(label=lab, file=os.path.relpath(path, ROOT), line=i,
                                     kind="REFERENCE", text=ln.strip()[:160]))
    with open("depaudit-ledger.tsv", "w") as f:
        f.write("label\tkind\tfile\tline\ttext\n")
        for r in rows:
            f.write("%s\t%s\t%s\t%d\t%s\n" % (r["label"], r["kind"], r["file"], r["line"], r["text"].replace("\t", " ")))
    refs = [r for r in rows if r["kind"] == "REFERENCE"]
    defs = [r for r in rows if r["kind"] == "DEFINITION"]
    print("definitions found:", len(defs), " references found:", len(refs))
    print("\n-- definition sites")
    for r in defs:
        print("  %-40s %s:%d" % (r["label"], r["file"], r["line"]))
    print("\n-- reference sites (downstream uses), by label")
    for lab in LABELS:
        rr = [r for r in refs if r["label"] == lab]
        if not rr:
            continue
        print("  %s : %d" % (lab, len(rr)))
        for r in rr:
            print("      %s:%d  %s" % (r["file"], r["line"], r["text"][:120]))

if __name__ == "__main__":
    main()
