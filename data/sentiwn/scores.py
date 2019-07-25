#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def main():
    data = map(lambda row: row.split('\t'), sys.stdin)
    for row in data:
        if row[0].startswith('#'):
            continue
        else:
            if len(row) != 4:
                sys.stderr.write('Bad formating on ID ' + str(row))
                sys.stderr.write('Len of sense: ' + str(row) + 'is ' + str(len(row)) + "\n\n")
            if row[0] == 's':
                of = "%08d-a" % (int(row[1]))
            else:
                of = "%08d-%s" % (int(row[1]), row[0])

            pos = row[2]
            neg = row[3]
            score = float(pos) - float(neg)
            print('{}\t{}'.format(of, score))


if __name__ == "__main__":
    main()
