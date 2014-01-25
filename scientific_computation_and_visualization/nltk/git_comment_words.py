# -*- coding:utf-8 -*-
from collections import Counter
from pprint import pprint
from string import punctuation
import nltk
import enchant


def get_word_counter(file_name):
    d = enchant.Dict("en_US")
    map(lambda char: d.remove(char), punctuation)
    counter = Counter()
    total_len = 0
    with open(file_name) as f:
        for line in f:
            tokens = nltk.word_tokenize(line.lower())
            counter.update(tokens)
            total_len += 1

    for key in counter.keys():
        if not d.check(key):
            counter.pop(key)
    return counter, total_len


counter, total_commits = get_word_counter('../data/commits.txt')

print total_commits
top = counter.most_common(40)
pprint(top)

# todo: skip conj using ntlk.pos_tag

import pygal

line_chart = pygal.HorizontalBar()
line_chart.title = 'top 25 words over %d commits' % total_commits
line_chart.config.x_labels = [each[0] for each in top][::-1]
line_chart.add('', [each[1] for each in top][::-1])

line_chart.render_to_file('bar_chart.svg')
