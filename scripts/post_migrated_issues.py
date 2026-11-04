"""Post the migrated preamble clusters as issues on the owning repository.

    python3 scripts/post_migrated_issues.py --dry-run          # parse and print only
    GITHUB_TOKEN=... python3 scripts/post_migrated_issues.py   # post

The bodies are read from docs/issue-migration/sage-extensions.md, where each
cluster carries a ```markdown block under its `### <title>` heading.  The token
is read from the environment and is never written, logged or echoed.
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

REGISTER = 'docs/issue-migration/sage-extensions.md'
DEFAULT_REPO = 'dzackgarza/sage-extensions'


def parse(path):
    text = open(path, encoding='utf-8').read()
    clusters = []
    for block in re.split(r'^### ', text, flags=re.M)[1:]:
        title = block.split('\n', 1)[0].strip()
        body = re.search(r'^```markdown\n(.*?)^```', block, flags=re.M | re.S)
        if body is None:
            continue
        clusters.append((title, body.group(1).rstrip() + '\n'))
    return clusters


def post(repo, token, title, body):
    request = urllib.request.Request(
        f'https://api.github.com/repos/{repo}/issues',
        data=json.dumps({'title': title, 'body': body}).encode(),
        headers={
            'Authorization': f'Bearer {token}',
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28',
            'Content-Type': 'application/json',
            'User-Agent': 'research-issue-migration',
        },
        method='POST',
    )
    with urllib.request.urlopen(request, timeout=60) as answer:
        return json.load(answer)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', default=DEFAULT_REPO)
    parser.add_argument('--register', default=REGISTER)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--only', default=None, help='post one cluster by title substring')
    options = parser.parse_args()

    clusters = parse(options.register)
    if options.only:
        clusters = [c for c in clusters if options.only.lower() in c[0].lower()]
    if not clusters:
        sys.exit(f'no clusters found in {options.register}')

    if options.dry_run:
        for title, body in clusters:
            print(f'--- {title} ({len(body.splitlines())} lines) ---')
            print(body[:400])
            print()
        print(f'{len(clusters)} clusters parsed; nothing posted')
        return

    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        sys.exit('GITHUB_TOKEN is not set')

    failures = 0
    for title, body in clusters:
        try:
            issue = post(options.repo, token, title, body)
        except urllib.error.HTTPError as error:
            detail = error.read().decode('utf-8', 'replace')[:400]
            print(f'FAILED  {title}: HTTP {error.code} {detail}')
            failures += 1
            continue
        except urllib.error.URLError as error:
            print(f'FAILED  {title}: {error.reason}')
            failures += 1
            continue
        print(f'created #{issue["number"]}  {issue["html_url"]}')

    if failures:
        sys.exit(f'{failures} of {len(clusters)} clusters were not created')


if __name__ == '__main__':
    main()
