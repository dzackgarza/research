"""Does `9-9-1_1.coxiter` encode the computed I_{1,8} chamber?

The question.  computations/reports/coble_I18_vinberg-chamber-run.txt computes the chamber of the
Coble cusp lattice, invariants (9, 9, 1), and prints its nine walls, their Gram matrix, and its
edges as `(i, j, label)` triples with label counts {3: 7, 4: 1} and degrees [1, 2, 3, 2, 2, 2, 2, 1, 1].
computations/coxiter/9-9-1_1.coxiter is the CoxIter input for that diagram, and its own transcript
logs/9-9-1_1.txt records finite covolume with one ideal vertex.  The two were never compared.  A
reading of the chamber as "a chain with two label-4 edges" was filed against the input; this record
decides it by comparing the two objects as edge-labelled graphs, with no relabelling assumed.

Objects compared:
  (record)  the `edges (i, j, label): ...` line and the `label counts` line of
            computations/reports/coble_I18_vinberg-chamber-run.txt, walls numbered 1..9;
  (input)   computations/coxiter/9-9-1_1.coxiter, nine vertices numbered 1..9.
An edge's label is its Coxeter exponent; the comparison is an isomorphism of edge-labelled graphs,
found by brute force over the degree classes, and it is asserted, not eyeballed.  CoxIter's own
verdict on the input is printed beside it, so the input's meaning and its reading are in one place.

Run:
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
      -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
      /repo/computations/reports/coble_I18-coxiter-input.py

Plain Python: neither object needs Sage.  Transcript: coble_I18-coxiter-input-run.txt.

The input's first line reads `dimension 9`, which declares nine vertices and leaves the dimension
unset, so CoxIter guesses; the guess is 8, which is the dimension of the hyperbolic space of a
rank-9 lattice with signature (1,8).  See the format paragraph of computations/coxiter/README.md.
"""
import re
import subprocess
from itertools import permutations, product

RECORD = '/repo/computations/reports/coble_I18_vinberg-chamber-run.txt'
INPUT = '/repo/computations/coxiter/9-9-1_1.coxiter'
COXITER = '/usr/local/bin/coxiter'

text = open(RECORD).read()
line = re.search(r'^  edges \(i, j, label\): (\[.*\])$', text, re.M)
assert line, 'edge line not found in the record'
record_edges = {(int(i), int(j), int(m)) for i, j, m in re.findall(r'\((\d+), (\d+), (\d+)\)', line.group(1))}
walls = int(re.search(r'^  walls: (\d+)$', text, re.M).group(1))
record_counts = {int(k): int(v) for k, v in re.findall(r'(\d+): (\d+)', re.search(r'^  label counts: (\{.*\})$', text, re.M).group(1))}

raw = [l.strip() for l in open(INPUT).read().splitlines() if l.strip()]
head = raw[0]
file_edges = {(int(u), int(v), int(m)) for u, v, m in (l.split() for l in raw[1:])}
vertices = max(max(u, v) for u, v, _ in file_edges)
input_counts = {}
for _, _, m in file_edges:
    input_counts[m] = input_counts.get(m, 0) + 1

print('record: %d walls, label counts %s' % (walls, dict(sorted(record_counts.items()))))
print('input:  first line %r, %d vertices, label counts %s'
      % (head, vertices, dict(sorted(input_counts.items()))))
print()


def labelled(E, n):
    d = {k: 0 for k in range(1, n + 1)}
    for a, b, _ in E:
        d[a] += 1
        d[b] += 1
    return {tuple(sorted((a, b))): m for a, b, m in E}, d


R, dr = labelled(record_edges, walls)
F, df = labelled(file_edges, vertices)
print('degrees  record %s' % [dr[k] for k in sorted(dr)])
print('degrees  input  %s' % [df[k] for k in sorted(df)])
assert sorted(dr.values()) == sorted(df.values()), 'degree sequences differ'
assert len(R) == len(F) == walls - 1, (len(R), len(F), walls)

assert record_counts == input_counts, (record_counts, input_counts)
classes = {}
for k, v in dr.items():
    classes.setdefault(v, []).append(k)
targets = {}
for k, v in df.items():
    targets.setdefault(v, []).append(k)
assert sorted(len(v) for v in classes.values()) == sorted(len(v) for v in targets.values())

phi_found = None
for choice in product(*[list(permutations(sorted(targets[d]))) for d in sorted(classes)]):
    phi = {}
    for d, perm in zip(sorted(classes), choice):
        phi.update(dict(zip(sorted(classes[d]), perm)))
    if all(F.get(tuple(sorted((phi[a], phi[b])))) == m for (a, b), m in R.items()):
        phi_found = phi
        break
print()
print('isomorphism record -> input: %s' % (phi_found,))
assert phi_found, 'the two are not isomorphic as edge-labelled graphs'
print()

run = subprocess.run([COXITER], input='\n'.join(raw) + '\n', capture_output=True, text=True)
assert run.returncode == 0, run.stdout + run.stderr
print('CoxIter on the input, no options:')
for l in run.stdout.splitlines():
    if any(k in l for k in ('Number of vertices', 'Dimension', 'Guessed', 'Finite covolume',
                            'Cocompact', 'f-vector', 'vertices at infinity', 'Field generated')):
        print('  %s' % l.strip())
assert 'Finite covolume: yes' in run.stdout
assert 'Number of vertices at infinity: 1' in run.stdout
print()
print('VERDICT: the input is the computed chamber as an edge-labelled graph -- nine walls, seven')
print('         label-3 edges and one label-4 edge. The "two label-4 edges" reading of the chamber')
print('         does not reproduce; nothing in the input or the record needs replacing.')
