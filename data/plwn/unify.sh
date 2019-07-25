#!/bin/bash

awk -F'\t' 'BEGIN {OFS="\t"} FNR==NR{keys[($1)]=$2;next} {print !($1 in keys) ? "x\t"$2 : keys[$1]"\t"$2;}' mapping-plwn-pwn.txt raw/synonymy.raw.txt | python unify.py | tee synonymy.txt
awk -F'\t' 'BEGIN {OFS="\t"} FNR==NR{keys[($1)]=$2;next} {print !($1 in keys) ? "x\t"$2 : keys[$1]"\t"$2;}' mapping-plwn-pwn.txt raw/hyponymy.raw.txt | python unify.py | tee hyponymy.txt
awk -F'\t' 'BEGIN {OFS="\t"} FNR==NR{keys[($1)]=$2;next} {print !($1 in keys) ? "x\t"$2 : keys[$1]"\t"$2;}' mapping-plwn-pwn.txt raw/hypernymy.raw.txt | python unify.py | tee hypernymy.txt
