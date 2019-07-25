#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
from bs4 import BeautifulSoup
from collections import defaultdict


np.set_printoptions(precision=3)


def read_scores_gen(filepath):
    with open(filepath) as ifile:
        soup = BeautifulSoup(ifile.read())
    for concept in soup.find_all('concept'):
        tag = concept.find('tag')
        doc = concept.parent.parent.attrs['doc']
        try:
            concept.attrs['synset_tag']
        except Exception:
            continue
        if tag:
            yield (doc,
                   concept.attrs['clemma'],
                   concept.attrs['synset_tag'],
                   tag.attrs['value'])
        else:
            yield (doc,
                   concept.attrs['clemma'],
                   concept.attrs['synset_tag'],
                   0.0)


def main():
    if len(sys.argv) != 2:
        sys.exit(-1)
    filepath = sys.argv[1]
    annotations = defaultdict(list)
    for doc, lemma, pwn_tag, sentiment in read_scores_gen(filepath):
        if doc not in ('spec', 'danc'):
            continue
        annotations[pwn_tag].append(sentiment)

    # average scores - averaging occurrences
    avg_scores = {}
    for pwn_tag, scores in annotations.items():
        avg_scores[pwn_tag] = sum(map(float, scores)) / len(scores)

    for pwn_tag, avg_score in avg_scores.items():
        print('{}\t{:.3f}'.format(pwn_tag, avg_score))


if __name__ == "__main__":
    main()
