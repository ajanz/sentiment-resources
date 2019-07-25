#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from scipy.stats import pearsonr


def load_data(filepath):
    data = {}
    with open(filepath) as ifile:
        for line in ifile:
            syn_id, annotation = line.strip().split('\t')
            data[syn_id] = annotation
    return data


def main():
    if len(sys.argv) != 3:
        sys.exit(-1)

    f_data = load_data(sys.argv[1])
    s_data = load_data(sys.argv[2])

    # intersect the keys to get only matched synsets
    keys = set.intersection(set(f_data.keys()), set(s_data.keys()))
    print('Intersection: {}'.format(len(keys)))
    f_ann = [float(f_data[key]) for key in keys]
    s_ann = [float(s_data[key]) for key in keys]

    corr, _ = pearsonr(f_ann, s_ann)
    print('Correlation: {}'.format(corr))


if __name__ == "__main__":
    main()
