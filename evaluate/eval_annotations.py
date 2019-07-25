#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from sklearn.metrics import cohen_kappa_score


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

    # print_out = True

    f_data = load_data(sys.argv[1])
    s_data = load_data(sys.argv[2])

    # intersect the keys to get only matched synsets
    keys = set.intersection(set(f_data.keys()), set(s_data.keys()))
    print('Matched: {}'.format(len(keys)))
    f_ann = [f_data[key] for key in keys]
    s_ann = [s_data[key] for key in keys]
    kappa = cohen_kappa_score(f_ann, s_ann)
    print('Kappa-2 score: {}'.format(kappa))

    # convert to 3-degree scale
    f_ann = [f_data[key].replace('m', '').replace('s', '') for key in keys]
    s_ann = [s_data[key].replace('m', '').replace('s', '') for key in keys]
    kappa = cohen_kappa_score(f_ann, s_ann)
    print('Kappa-1 score: {}'.format(kappa))

    # if print_out:
    #     for key in keys:
    #         if f_data[key] == s_data[key]:
    #             print("{}\t{}".format(key, f_data[key]))


if __name__ == "__main__":
    main()
