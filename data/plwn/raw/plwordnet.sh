#!/bin/bash

# query:
# 	    *parent*	      *child*
# pl[LU] --- pl[SYN] -[rel]-> en[SYN]
#   |
# emo[LU]


# synonymy
# 198:	i-synonymy (general)
# 208:	i-synonymy (PWN - plWN)
# 209:	i-synonymy (plWN - PWN)
# 3006:	partial i-synonymy (general)
# 3005: partial i-synonymy (PWN - plWN)
# 3004: partial i-synonymy (plWN - PWN)
# 238:	paradigmatic i-synonymy (resembling)
# 235:	paradigmatic i-synonymy (made of)
# 239:	paradigmatic i-synonymy (related to)
rel_ids="198, 208, 209, 3006, 3005, 3004, 238, 235, 239"

query="SELECT rel.child_id, emo.markedness FROM emotion AS emo \
	JOIN unitandsynset  AS uas ON emo.lexicalunit_id = uas.lex_id \
	JOIN synsetrelation AS rel ON uas.syn_id = rel.parent_id \
	WHERE rel.rel_id in (rel_ids);"

echo ${query/rel_ids/${rel_ids}} | mycli -u wordnet -D 2019_02_28_plwn | tee synonymy.raw.txt

# hyponymy
# 210: hyponymy (plWN-PWN)
# 214: hipernym (PWN-plWN)
# 227: interreg synonymy (general)
# 228: interreg synonymy (plWN-PWN)
# 229: interreg synonymy (PWN-plWN)
rel_ids="210, 214, 227, 228, 229"

echo ${query/rel_ids/${rel_ids}} | mycli -u wordnet -D 2019_02_28_plwn | tee hyponymy.raw.txt

# hypernymy
# 211: hyponymy (PWN-plWN)
# 212: hypernym (plWN-PWN)
rel_ids="211, 212"
echo ${query/rel_ids/${rel_ids}} | mycli -u wordnet -D 2019_02_28_plwn | tee hypernymy.raw.txt
