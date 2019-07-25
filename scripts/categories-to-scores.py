#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def main():
    mapping = {
        '+m': 0.8,
        '+s': 0.4,
        'n': 0.0,
        '-s': -0.4,
        '-m': -0.8,
        # 'amb': 'U'
    }
    for line in sys.stdin:
        sid, val = line.strip().split('\t')
        cat = val.strip()
        try:
            print('{}\t{}'.format(sid, mapping[cat]))
        except KeyError:
            continue


if __name__ == "__main__":
    main()
