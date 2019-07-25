#!/bin/bash

echo "SentiWN - MLSentiCon"
python evaluate/eval_scores.py data/sentiwn/sentiwn.scores data/mlsenticon/senticon.scores

echo "NTUMC - SentiWN"
python evaluate/eval_scores.py data/ntumc/ntumc.scores data/sentiwn/sentiwn.scores

echo "NTUMC - MLSentiCon"
python evaluate/eval_scores.py data/ntumc/ntumc.scores data/mlsenticon/senticon.scores

echo "plWN - SentiWN"
python evaluate/eval_scores.py data/plwn/plwn.synonymy.scores data/sentiwn/sentiwn.scores

echo "plWN - MLSentiCon"
python evaluate/eval_scores.py data/plwn/plwn.synonymy.scores data/mlsenticon/senticon.scores

echo "plWN - NTUMC"
python evaluate/eval_scores.py data/plwn/plwn.synonymy.scores data/ntumc/ntumc.scores
