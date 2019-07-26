#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def avg(scores):
    return sum(score for score in scores) / float(len(scores))


def main():
    if len(sys.argv) != 3:
        sys.exit(-2)
    f_file, s_file = sys.argv[1], sys.argv[2]
    f_scores, s_scores = {}, {}
    with open(f_file) as ifile:
        for line in ifile:
            sid, score = line.strip().split('\t')
            f_scores[sid] = float(score)

    with open(s_file) as ifile:
        for line in ifile:
            sid, score = line.strip().split('\t')
            s_scores[sid] = float(score)

    # just intersection of keys
    # keys = set.intersection(set(f_scores.keys()), set(s_scores.keys()))
    # for key in keys:
    #     score = avg([f_scores[key], s_scores[key]])
    #     print('{}\t{}'.format(key, score))

    # union of keys
    keys = set.union(set(f_scores.keys()), set(s_scores.keys()))
    for key in keys:
        if (key in s_scores) and (key in f_scores):
            score = avg([f_scores[key], s_scores[key]])
        else:
            try:
                score = f_scores[key]
            except KeyError:
                score = s_scores[key]
        print('{}\t{}'.format(key, score))


if __name__ == "__main__":
    main()
