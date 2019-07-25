#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def main():
    data = map(lambda row: row.split('\t'), sys.stdin)
    func = None
    for row in data:
        if row[0].startswith('# begin Common'):
            # compute the scores of group 'Common'
            func = apply_common
        elif row[0].startswith('# begin Group1'):
            # compute the scores of group 'Group1'
            func = apply_group1
        elif row[0].startswith('# begin Group2'):
            # compute the scores of group 'Group2'
            func = apply_group2
        if row[0].startswith('#'):
            continue
        of = "%08d-%s" % (int(row[-1][1:]), row[-1][0])
        score = func(row)
        print('{}\t{}'.format(of, score))


def apply_common(row):
    pos = float(row[0])
    neg = float(row[1])
    return pos - neg


def apply_group1(row):
    pos1 = float(row[0])
    neg1 = float(row[1])

    pos2 = float(row[2])
    neg2 = float(row[3])

    pos3 = float(row[4])
    neg3 = float(row[5])
    return ((pos1 + pos2 + pos3) / 3) - ((neg1 + neg2 + neg3) / 3)


def apply_group2(row):
    pos1 = float(row[0])
    neg1 = float(row[1])

    pos2 = float(row[2])
    neg2 = float(row[3])
    return ((pos1 + pos2) / 2) - ((neg1 + neg2) / 2)


if __name__ == "__main__":
    main()
