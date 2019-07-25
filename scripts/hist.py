#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np


def main():
    data = map(lambda row: row.split('\t'), sys.stdin)
    data = list(map(lambda row: float(row[1].strip()), data))
    hist = np.histogram(data)

    for count, value in zip(hist[0], hist[1]):
        print('{}\t{}'.format(count, value))


if __name__ == "__main__":
    main()
