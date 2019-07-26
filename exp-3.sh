#!/bin/bash

echo "MWNOp - plWN"
python evaluate/eval_scores.py data/mwnop/mwnop.scores data/plwn/plwn.synonymy.scores

echo "MWNOp - NTUMC"
python evaluate/eval_scores.py data/mwnop/mwnop.scores data/ntumc/ntumc.scores

echo "MWNOp - SentiWN"
python evaluate/eval_scores.py data/mwnop/mwnop.scores data/sentiwn/sentiwn.scores

# joint lexicon of plWN & NTUMC
echo "MWNOp - plWN & NTUMC"
python evaluate/eval_scores.py data/mwnop/mwnop.scores <(python scripts/join_scores.py data/plwn/plwn.synonymy.scores data/ntumc/ntumc.scores)
