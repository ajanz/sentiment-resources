#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def main():
    mapping = {
        (0.55, 1.00): '+m',
        (0.18, 0.55): '+s',
        (-0.18, 0.18): 'n',
        (-0.55, -0.18): '-s',
        (-1.00, -0.55): '-m'
    }
    for line in sys.stdin:
        sid, val = line.strip().split('\t')
        try:
            score = float(val.strip())
        except ValueError:
            continue
        for srange, ann in mapping.items():
            if srange[0] < score <= srange[1]:
                print('{}\t{}'.format(sid, ann))


if __name__ == "__main__":
    main()
