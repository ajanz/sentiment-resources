#!/bin/bash

echo "plWN(synonymy) - NTUMC"
python evaluate/eval_scores.py data/plwn/plwn.synonymy.scores data/ntumc/ntumc.scores

echo "plWN(hyponymy) - NTUMC"
python evaluate/eval_scores.py data/plwn/plwn.hyponymy.scores data/ntumc/ntumc.scores

echo "plWN(hypernymy) - NTUMC"
python evaluate/eval_scores.py data/plwn/plwn.hypernymy.scores data/ntumc/ntumc.scores
