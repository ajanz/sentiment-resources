#!/bin/bash

echo "plWN(synonymy) - NTUMC"
python evaluate/eval_scores.py data/plwn/plwn.synonymy.scores data/ntumc/ntumc.scores
python evaluate/eval_annotations.py data/plwn/out/synonymy.txt data/ntumc/ntumc.cats

echo "plWN(hyponymy) - NTUMC"
python evaluate/eval_scores.py data/plwn/plwn.hyponymy.scores data/ntumc/ntumc.scores
python evaluate/eval_annotations.py data/plwn/out/hyponymy.txt data/ntumc/ntumc.cats

echo "plWN(hypernymy) - NTUMC"
python evaluate/eval_scores.py data/plwn/plwn.hypernymy.scores data/ntumc/ntumc.scores
python evaluate/eval_annotations.py data/plwn/out/hypernymy.txt data/ntumc/ntumc.cats
