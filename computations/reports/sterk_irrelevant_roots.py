import re
src = open('.scratch/se-api/src/sage_extensions/sterk.py').read()
block = src[src.index('configurations = {'):src.index('configurations = {', src.index('configurations = {')+1)]
block = src[src.index('"Sterk_1": ('):src.index('        }\n        configurations = {')]
# split per cusp
parts = re.split(r'"Sterk_(\d)": \(', block)[1:]
# Figure 5, square panel: boundary alpha_0..alpha_15, interior alpha_16..alpha_21, and
# alpha_i = v_{i+1}.  Triangle panel: boundary alpha_2..alpha_18, interior alpha_1 and alpha_19,
# with alpha_1 = w18, alpha_i = w_{i-1} for 2 <= i <= 18, and alpha_19 = w19.  Double circles in
# the figure mark boundary parity, not irrelevance.
INTERIOR = set(range(16, 22))          # square, in alpha
TRIANGLE_INTERIOR = {18, 19}           # triangle, in w
for k in range(0, len(parts), 2):
    name, body = parts[k], parts[k+1]
    entries = re.findall(r'v\["v(\d+)"\]|w\["w(\d+)"\]|orbit_sum\(v\["v(\d+)"\]\)', body)
    # simpler: split body into top-level terms
    terms, depth, cur, in_str = [], 0, '', False
    cleaned = body.split('\n            ),')[0]
    for ch in cleaned:
        if ch == '(':
            depth += 1
        if ch == ')':
            depth -= 1
        if ch == ',' and depth == 0:
            terms.append(cur.strip()); cur = ''
        else:
            cur += ch
    if cur.strip():
        terms.append(cur.strip())
    print('Sterk_%s: %d folded roots' % (name, len(terms)))
    irrelevant = []
    for i, term in enumerate(terms, start=1):
        vnums = {int(x) for x in re.findall(r'v\["v(\d+)"\]', term)}
        wnums = {int(x) for x in re.findall(r'w\["w(\d+)"\]', term)}
        if vnums:
            figures = {n - 1 for n in vnums}
            if figures <= INTERIOR or vnums <= {n + 1 for n in INTERIOR}:
                irrelevant.append((i, sorted(figures)))
        elif wnums:
            if wnums <= TRIANGLE_INTERIOR:
                irrelevant.append((i, sorted(wnums)))
    print('   irrelevant by Figure 5 non-boundary vertices: roots %s' % ([i for i, _ in irrelevant],))
    for i, figures in irrelevant:
        print('      root %d <- figure vertices %s' % (i, figures))
