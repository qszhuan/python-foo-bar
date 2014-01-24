# -*- coding:utf-8 -*-
from collections import Counter
import os
from pprint import pprint
from string import maketrans, translate
import nltk
import enchant

d = enchant.Dict("en_US")

trans_pattern_well = maketrans(']|: ', '    ')

with open('../data/commits.txt') as f:
    commits = f.readlines()
    lines_without_changset = [line.split(' ', 1)[1].strip().lower() for line in commits]

comments = []
for line in lines_without_changset:
    line_with_plain_sep = translate(line, trans_pattern_well).strip()
    pair = line_with_plain_sep.split(' ', 1)
    if d.check(pair[0]):
        comments.append(line_with_plain_sep)
    else:
        comments.append(pair[-1])

#check results manually
#zips = zip(comments, lines_without_changset)
#pprint(zips)


word_counter = Counter()
freq_dist = nltk.FreqDist()

for line in comments:
    tokens = nltk.word_tokenize(line)
    tags = nltk.pos_tag(tokens)
    for word, tag in tags:
        if 'V' in tag or 'N' in tag:
            freq_dist.inc(word)
        #else:
        #    print word, tag

for skip_word in ['of', 'in', 'for', 'from', 'n/a', 'before', 'by', 'via']:
    freq_dist.pop(skip_word)
pprint(freq_dist.items()[:30])
exit()
    #word_counter.update(tokens)

pprint(word_counter.most_common(20))

pprint(nltk.pos_tag(word_counter.keys()))

for word, _ in word_counter.most_common(100):
    if nltk.pos_tag([word])[0][-1][0] not in ['V', 'N']:
        print word, _
        word_counter.pop(word)


