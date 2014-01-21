# -*- coding:utf-8 -*-
from collections import Counter
import os
from pprint import pprint
from string import maketrans, uppercase, punctuation, lowercase, translate
import itertools

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
         'ql':'yql',

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
         'tz':'zhangtong',

         'wj':'wangjian',

         'xj': 'xianjing',
         'xjz': 'xianjing',

         'zy': 'zhuyu',
         'yu': 'zhuyu',
         'yzhu': 'zhuyu',
         'zyu':'zhuyu',

         'rj': 'ruijie',

         'hj': 'yhj',
         'haijiao':'yhj',

         'zsw': 'shiwei',
         'sw': 'shiwei',

         'xin': 'lixin',
         'linxin':'lixin',

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
         'ganghe':'hegang',

         'yannjun': 'yanjun',

         'gb':'gerard',


}

trans_pattern = maketrans(uppercase + punctuation, lowercase + ' ' * len(punctuation))
trans_pattern_well = maketrans('|:', '  ')

with open('tiger.commits') as f:
    commits = f.readlines()
    lines = [line.split(' ', 1)[1] for line in commits]
counter = Counter()
commit_counter = Counter()

for each in lines:
    each = each.lstrip().rstrip(os.linesep)
    if each.startswith('['):
        persons= each.split(']')[0]
        if each.endswith(']'):
            print "$$$", each
            continue
        pairs = translate(persons, trans_pattern).split()
    else:
        pairs = translate(each, trans_pattern_well).split(' ', 1)[0]
        pairs = translate(pairs, trans_pattern).split()

    if len(pairs) < 2:
        #print '#####', pairs, each
        continue
    skip_keywords = {'a', 'introduce', 'fix', 'clear', 'delete', 'regression', 'service', 'organize', 'build', 'object', 'and', 'a'}
    if skip_keywords.intersection(pairs):
        print '@@', pairs, each
        continue

    for index, value in enumerate(pairs):
        pairs[index] = vests.get(value, value)

    pairs = sorted(pairs)
    commit_counter.update(pairs)
    combs = list(itertools.combinations(pairs, 2))
    counter.update(combs)

pprint(counter.most_common())
pprint(commit_counter.most_common())

print '*****', set(commit_counter.keys()).difference(set(vests.keys() + vests.values()))

with open('pairs.txt', 'w') as p:
    p.write('*' * 80 + os.linesep)
    pprint(counter.most_common(10), p)
    p.write('*' * 80 + os.linesep)
    pprint(commit_counter.most_common(10), p)