import re
src = open('.scratch/se-api/src/sage_extensions/sterk.py').read()
block = src[src.index('configurations = {'):src.index('configurations = {', src.index('configurations = {')+1)]
block = src[src.index('"Sterk_1": ('):src.index('        }\n        configurations = {')]
# split per cusp
parts = re.split(r'"Sterk_(\d)": \(', block)[1:]
INTERIOR = set(range(16, 22))     # figure vertices 16..21, i.e. v17..v22 under v_i <-> figure i-1
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
            if figures <= INTERIOR:
                irrelevant.append((i, sorted(figures)))
        elif wnums:
            pass
    print('   irrelevant by Figure 5 non-boundary vertices: r_%s' % ([i for i, _ in irrelevant],))
    for i, figures in irrelevant:
        print('      r_%d <- figure vertices %s' % (i, figures))
