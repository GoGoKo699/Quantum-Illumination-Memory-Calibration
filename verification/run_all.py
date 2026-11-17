#!/usr/bin/env python3
"""Run required scientific checks and record their exact source boundaries."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    checks = []
    for name in ('certify_constants.py', 'check_count_laws.py', 'check_receiver.py'):
        result = subprocess.run([sys.executable, str(ROOT / 'verification' / name)],
                                cwd=ROOT, text=True, capture_output=True)
        if result.returncode:
            print(result.stdout)
            print(result.stderr, file=sys.stderr)
            raise SystemExit(result.returncode)
        checks.append({'program': name, 'status': 'passed'})
        print(f'PASS: {name}')
    missing = []
    for page in ROOT.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', page.read_text()):
            target = target.split('#', 1)[0].strip('<>')
            if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                continue
            if not (page.parent / target).exists():
                missing.append(f'{page.relative_to(ROOT)} -> {target}')
    if missing:
        raise SystemExit('Broken local reader links:\n' + '\n'.join(missing))
    sources = {}
    for path in sorted(ROOT.rglob('*')):
        if path.is_file() and path.suffix in ('.py', '.md', '.bib', '.txt', '.yml'):
            sources[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    report = {'status': 'passed', 'checks': checks, 'local_reader_links': 'passed',
              'source_sha256': sources,
              'scope': 'Exact constants, finite count laws and selected diagnostics; analytical proofs remain authoritative.'}
    (ROOT / 'verification/verification_report.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(f'PASS: local reader links; {len(sources)} source hashes recorded')


if __name__ == '__main__':
    main()
