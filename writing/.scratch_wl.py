import re, pathlib, sys

ROOT = pathlib.Path('.')
PARTS = ['category-theory', 'coble', 'lattice-theory', 'data', 'index.md']

def pages():
    out = []
    for part in PARTS:
        p = ROOT / part
        if p.is_file(): out.append(p)
        else: out.extend(sorted(p.rglob('*.md')))
    return out

def title_and_anchor(p):
    for line in p.read_text(errors='replace').splitlines():
        m = re.match(r'^#\s+(.*)$', line)
        if m:
            anchor = re.search(r'\{#([^}]+)\}', line)
            title = re.sub(r'\s*\{#[^}]+\}', '', m.group(1)).replace('$', '').strip()
            return title, (anchor.group(1) if anchor else None)
        if line.startswith('---'): pass
    return None, None

def main(apply):
    ps = pages()
    by_stem = {}
    for p in ps: by_stem.setdefault(p.stem, p)
    changes = []
    for p in ps:
        text = p.read_text()
        body_start = 0
        if text.startswith('---\n'):
            end = text.find('\n---\n', 3)
            if end != -1: body_start = end + 5
        head, body = text[:body_start], text[body_start:]
        lines = body.split('\n')
        in_fence = False
        out_lines = []
        for line in lines:
            if line.lstrip().startswith('```'):
                in_fence = not in_fence; out_lines.append(line); continue
            if in_fence or '[[' not in line:
                out_lines.append(line); continue
            # protect inline code and math
            slots = []
            def keep(m):
                slots.append(m.group(0)); return f'\x00{len(slots)-1}\x00'
            prot = re.sub(r'`[^`]*`|\$\$.*?\$\$|\$[^$]*\$', keep, line)
            def repl(m):
                target, disp = m.group(1).strip(), (m.group(3) or '').strip()
                stem = target[:-3] if target.endswith('.md') else target
                stem = stem.split('/')[-1]
                page = by_stem.get(stem)
                if page is None:
                    return m.group(0)  # leave; reported below
                t, a = title_and_anchor(page)
                if a is None:
                    return m.group(0)
                if not disp: disp = t
                return f'[{disp}](#{a})'
            new = re.sub(r'\[\[([^\]|]+)(\|([^\]]*))?\]\]', repl, prot)
            for i, s in enumerate(slots):
                new = new.replace(f'\x00{i}\x00', s)
            if new != line:
                changes.append((str(p), line.strip()[:70], new.strip()[:90]))
            out_lines.append(new)
        if out_lines != lines and apply:
            p.write_text(head + '\n'.join(out_lines))
    print(f'{len(changes)} lines rewritten')
    for c in changes[:int(sys.argv[2]) if len(sys.argv)>2 else 12]:
        print(f'  {c[0]}\n    - {c[1]}\n    + {c[2]}')
    return changes

if __name__ == '__main__':
    main(apply=sys.argv[1] == 'apply')
