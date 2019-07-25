#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This script analyses the annotations of plWordNet LUs to generate
the annotations (emotive categories) for synsets (-m, -s, n, +s, +m).
"""
import sys
from collections import defaultdict, Counter


when_equal = {
    frozenset({'amb', 'n'}): 'amb',
    frozenset({'amb', '-s'}): 'amb',
    frozenset({'amb', '+s'}): 'amb',
    frozenset({'amb', '-m'}): 'amb',
    frozenset({'amb', '+m'}): 'amb',
    frozenset({'n', '-s'}): 'amb',
    frozenset({'n', '+s'}): 'amb',
    frozenset({'n', '-m'}): 'amb',
    frozenset({'n', '+m'}): 'amb',
    frozenset({'-s', '-m'}): '-s',
    frozenset({'+s', '+m'}): '+s',
    frozenset({'+s', '-s'}): 'amb',
    frozenset({'+m', '-m'}): 'amb',
    frozenset({'+m', '-s'}): 'amb',
    frozenset({'-m', '+s'}): 'amb'
}


def merge(syn_id, annotations):
    counts = Counter(annotations)
    top_annotation = max(counts, key=counts.get)
    top_count = counts[top_annotation]

    for annotation in annotations:
        # check if there exists another category with the same score
        if counts[annotation] == top_count and annotation != top_annotation:
            pair = {top_annotation, annotation}
            try:
                return when_equal[frozenset(pair)]
            except KeyError:
                continue
    return top_annotation


def merge_annotations(lus_data):
    syn_data = set()
    for syn_id, annotations in lus_data.items():
        if len(annotations) == 1:
            syn_annotation = next(iter(annotations))
            syn_data.add((syn_id, syn_annotation))
        else:
            syn_annotation = merge(syn_id, annotations)
            syn_data.add((syn_id, syn_annotation))
    return sorted(syn_data)


def main():
    raw_data = map(lambda row: row.strip().split('\t'), sys.stdin)
    lus_data = defaultdict(list)
    for row in raw_data:
        syn_id, annotation = row
        lus_data[syn_id].append(annotation)

    syn_data = merge_annotations(lus_data)
    for syn_id, annotation in syn_data:
        print('{}\t{}'.format(syn_id, annotation))


if __name__ == "__main__":
    main()
