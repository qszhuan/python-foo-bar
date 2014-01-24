# -*- coding:utf-8 -*-
from collections import Counter
from math import sqrt, ceil
import os
from pprint import pprint
from string import maketrans, uppercase, punctuation, lowercase, translate
import itertools
import matplotlib.pyplot as plt


vests = {'ah': 'anhui',

         'bin': 'binli',
         'libin': 'binli',

         'cc': 'chao',
         'wangchao': 'chao',
         'wc': 'chao',
         'hcheng': 'chenghong',
         'ch': 'chenghong',

         'fyr': 'yingrui',
         'yr': 'yingrui',
         'yrfeng': 'yingrui',

         'hz': 'hongzhang',
         'lhz': 'hongzhang',

         'jy': 'jiayang',

         'liying': 'lly',
         'ly': 'lly',

         'mingwe': 'mingwei',
         'mw': 'mingwei',
         'pmw': 'mingwei',

         'qiang': 'xqyu',
         'xiaoqiang': 'xqyu',
         'xyqu': 'xqyu',
         'yxq': 'xqyu',
         'xqiang': 'xqyu',

         'qilin': 'yql',
         'qinlin': 'yql',
         'ql': 'yql',

         'zx': 'zhangxiang',
         'zj': 'jun',
         'junjun': 'jun',

         'zq': 'zhengquan',

         'qingshan': 'qszhuan',
         'qs': 'qszhuan',
         'qszhan': 'qszhuan',

         'ss': 'shasha',

         'tong': 'zhangtong',
         'zt': 'zhangtong',
         'tzhang': 'zhangtong',
         'tz': 'zhangtong',

         'wj': 'wangjian',

         'xj': 'xianjing',
         'xjz': 'xianjing',

         'zy': 'zhuyu',
         'yu': 'zhuyu',
         'yzhu': 'zhuyu',
         'zyu': 'zhuyu',

         'rj': 'ruijie',

         'hj': 'yhj',
         'haijiao': 'yhj',

         'zsw': 'shiwei',
         'sw': 'shiwei',

         'xin': 'lixin',
         'linxin': 'lixin',

         'xh': 'huangxin',
         'xhuang': 'huangxin',
         'hx': 'huangxin',
         'xinhuang': 'huangxin',

         'zz': 'zhezi',

         'rm': 'zrm',

         'juliio': 'julio',

         'gt': 'guangtao',
         'ygt': 'guangtao',


         'gh': 'hegang',
         'hg': 'hegang',
         'ganghe': 'hegang',

         'yannjun': 'yanjun',

         'gb': 'gerard',

         'qihui': 'qq',

         'cx': 'xi'


}

trans_pattern = maketrans(uppercase + punctuation, lowercase + ' ' * len(punctuation))
trans_pattern_well = maketrans('|:', '  ')

with open('commits.txt') as f:
    commits = f.readlines()
    lines = [line.split(' ', 1)[1].lstrip().rstrip(os.linesep) for line in commits]
pair_counter = Counter()
commit_counter_per_person = Counter()
words_counter = Counter()
for each in lines:
    if each.startswith('['):
        persons, comment = each.split(']', 1)

        if each.endswith(']'):
            print "$$$", each
            continue
        pairs = translate(persons, trans_pattern).split()
    else:
        pair_comments = translate(each, trans_pattern_well).split(' ', 1)
        if len(pair_comments) == 1:
            comment = pair_comments[0]
        else:
            pairs, comment = pair_comments
            pairs = translate(pairs, trans_pattern).split()

    words = translate(comment, trans_pattern).split(' ')
    words_real = [each for each in words if each is not '']
    words_counter.update(words_real)

    if len(pairs) < 2:
        continue
    skip_keywords = {'a', 'introduce', 'fix', 'clear', 'delete', 'regression', 'service', 'organize', 'build', 'object',
                     'and', 'a'}
    if skip_keywords.intersection(pairs):
        print '@@', pairs, each
        continue

    for index, value in enumerate(pairs):
        pairs[index] = vests.get(value, value)

    pairs = sorted(pairs)
    commit_counter_per_person.update(pairs)
    combs = list(itertools.combinations(pairs, 2))
    pair_counter.update(combs)

# pprint(counter.most_common())
# pprint(commit_counter.most_common())

print '*****', set(commit_counter_per_person.keys()).difference(set(vests.keys() + vests.values()))

with open('pairs.txt', 'w') as p:
    p.write('*' * 80 + os.linesep)
    pprint(pair_counter.most_common(10), p)
    p.write('*' * 80 + os.linesep)
    pprint(commit_counter_per_person.most_common(10), p)

pair_rel = pair_counter.keys()
pprint(pair_rel)

relation_counter = Counter()
for each in pair_rel:
    relation_counter.update(each)

popular_workers = relation_counter.most_common(9)
pprint(words_counter.most_common())
#exit()

import networkx as nx


def draw_graph(graph, graph_layout='shell',
               node_size=1600, node_color='blue', node_alpha=0.3,
               node_text_size=14,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               text_font='sans-serif'):
    G = nx.Graph()

    G.add_edges_from(graph)

    if graph_layout == 'spring':
        graph_pos = nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos = nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos = nx.random_layout(G)
    else:
        graph_pos = nx.shell_layout(G)

    nx.draw_networkx_nodes(G, graph_pos, node_size=node_size, alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G, graph_pos, width=edge_tickness, alpha=edge_alpha, edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos, font_size=node_text_size, font_family=text_font)

    # if labels is None:
    #     labels = range(len(graph))
    #
    # edge_labels = dict(zip(graph, labels))
    # nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels,
    #                              label_pos=edge_text_pos)

    # show graph


count = len(popular_workers)
col = row = ceil(sqrt(count))
print col, row, count

plt.axis('off')
plt.figure(figsize=(18, 18))
for index, each in enumerate(popular_workers):
    plot = plt.subplot(col, row, index + 1)
    plot.axis('off')
    pw = each[0]
    pw_rel = [pair for pair in pair_counter.keys() if pw in pair]

    draw_graph(pw_rel, graph_layout='spring')

plt.savefig("most_pop_person.png", bbox_inches='tight')
