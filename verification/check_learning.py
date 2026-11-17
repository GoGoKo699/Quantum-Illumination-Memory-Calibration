#!/usr/bin/env python3
"""Validate the shared map's cardinality, fields and dependency order."""
from pathlib import Path
from fractions import Fraction
from math import comb
import re

ROOT=Path(__file__).resolve().parents[1]


def main():
    text=(ROOT/'learning/milestones.md').read_text()
    parts=re.split(r'^### (M\d{2})[^\n]*\n',text,flags=re.M)
    ids=parts[1::2]
    if ids!=[f'M{i:02d}' for i in range(1,31)]:
        raise SystemExit('Expected exactly M01 through M30 in order')
    fields=('Central question','Understanding target','Dependencies and story role',
            'Conceptual connection','Sources and project route')
    for id,body in zip(ids,parts[2::2]):
        for field in fields:
            if f'**{field}:**' not in body:
                raise SystemExit(f'{id}: missing {field}')
        dep=re.search(r'\*\*Dependencies and story role:\*\*([^\n]*)',body).group(1)
        for match in re.finditer(r'M(\d{2})(?:[–-]M?(\d{2}))?',dep):
            start=int(match[1]);end=int(match[2] or match[1])
            if not 1<=start<=end<int(id[1:]):
                raise SystemExit(f'{id}: invalid dependency {match[0]}')
    for filename in ('README.md','bridge.md','milestones.md'):
        source=(ROOT/'learning'/filename).read_text()
        if 'Weedbrook' not in source or '1110.3234v1' not in source:
            raise SystemExit(f'{filename}: selected source/version missing')
        if 'Revise → Learn → Test' in source or 'COACHING.md' in source:
            raise SystemExit(f'{filename}: personal coaching belongs outside the shared map')
    assert Fraction(comb(4,3),comb(6,3))==Fraction(1,5)
    assert Fraction(comb(3,3),comb(6,3))==Fraction(1,20)
    print('PASS: 30 milestones, five fields each, backward dependencies, selected anchor and worked count example')


if __name__=='__main__':
    main()
