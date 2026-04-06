#!/usr/bin/env python3
"""Validate agent markdown frontmatter in .github/agents.

This script performs lightweight checks without external deps:
- frontmatter exists between leading '---' markers
- required keys exist: description, model, tools, target, handoffs
- no trailing whitespace
- max line length recommendation (120 chars) -- warnings

Exit code 0 on success, 1 on failure.
"""
import os
import re
import sys


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENTS_DIR = os.path.join(ROOT, '.github', 'agents')

REQ_KEYS = ['description', 'model', 'tools', 'target', 'handoffs']


def find_md_files(path):
    for dirpath, _, filenames in os.walk(path):
        for fn in filenames:
            if fn.lower().endswith('.md'):
                yield os.path.join(dirpath, fn)


def extract_frontmatter(text):
    m = re.search(r'^---\s*\n(.*?)\n---\s*\n', text, re.S | re.M)
    if not m:
        return None
    return m.group(1)


def check_file(path):
    errors = []
    warnings = []
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # trailing whitespace
    for i, line in enumerate(text.splitlines(), start=1):
        if line.rstrip('\r\n') != line.rstrip():
            errors.append(f'{path}:{i}: trailing whitespace')
        if len(line) > 120:
            warnings.append(f'{path}:{i}: line length {len(line)} > 120')

    fm = extract_frontmatter(text)
    if fm is None:
        errors.append(f'{path}: missing or malformed frontmatter')
        return errors, warnings

    # crude key existence check (key: at line start)
    for key in REQ_KEYS:
        if not re.search(rf'^\s*{re.escape(key)}\s*:\s*', fm, re.M):
            errors.append(f'{path}: frontmatter missing required key: {key}')

    # description non-empty check
    m = re.search(r'^\s*description\s*:\s*(.+)$', fm, re.M)
    if m:
        val = m.group(1).strip()
        if val in ('', '""', "''"):
            errors.append(f'{path}: description appears empty')
    else:
        errors.append(f'{path}: description missing or empty')

    return errors, warnings


def main():
    if not os.path.isdir(AGENTS_DIR):
        print('No agents directory found, skipping.')
        return 0

    any_errors = False
    for md in find_md_files(AGENTS_DIR):
        errors, warnings = check_file(md)
        for w in warnings:
            print('WARNING:', w)
        for e in errors:
            print('ERROR:', e)
        if errors:
            any_errors = True

    if any_errors:
        print('\nFrontmatter validation failed.')
        return 1
    print('All agent frontmatter checks passed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
