# -*- coding:utf-8 -*-
import os
from pprint import pprint
from string import maketrans, punctuation, translate, uppercase, lowercase
import itertools
import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(graph, labels=None, graph_layout='shell',
               node_size=1600, node_color='blue', node_alpha=0.3,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):
    # create networkx graph
    G = nx.Graph()

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # these are different layouts for the network you may try
    # shell seems to work best
    if graph_layout == 'spring':
        graph_pos = nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos = nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos = nx.random_layout(G)
    else:
        graph_pos = nx.shell_layout(G)

    # draw graph
    nx.draw_networkx_nodes(G, graph_pos, node_size=node_size,
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G, graph_pos, width=edge_tickness,
                           alpha=edge_alpha, edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos, font_size=node_text_size,
                            font_family=text_font)

    if labels is None:
        labels = range(len(graph))

    edge_labels = dict(zip(graph, labels))
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels,
                                 label_pos=edge_text_pos)

    # show graph
    plt.show()

######################################
vests = {'ah': 'anhui',

         'bin': 'binli',
         'libin': 'binli',

         'cc': 'chao',
         'wangchao': 'chao',
         'wc': 'chao',
         'hcheng': 'ch',
         'chenghong': 'ch',

         'yingrui': 'fyr',
         'yr': 'fyr',
         'hongzhang': 'hz',

         'jiayang': 'jy',

         'liying': 'lly',
         'ly': 'lly',
         'mingwe': 'mingwei',
         'mw': 'mingwei',
         'qiang': 'xqyu',
         'xiaoqiang': 'xqyu',
         'yxq': 'xqyu',
         'qilin': 'yql',
         'zhangxiang': 'zx',
         'zj': 'jun',

         'qingshan': 'qszhuan',
         'qs': 'qszhuan',
         'shasha': 'ss',


         'xj': 'xianjing'}
######################################
trans_pattern = maketrans(uppercase + punctuation, lowercase + ' ' * len(punctuation))
trans_pattern_well = maketrans('|:_', '   ')

with open('commits.txt') as f:
    commits = f.readlines()
    lines = [line.split(' ', 1)[1] for line in commits]

    results = []
    result_set = set()
    for each in lines:
        if each.startswith('['):
            persons = each.split(']')[0]
            pairs = translate(persons, trans_pattern).split()
        else:
            pairs = translate(each, trans_pattern_well).split(' ', 1)[0]
            pairs = translate(pairs, trans_pattern).split()

        count = len(pairs)
        if count < 2:
            continue
        if 'clear' in pairs:
            print '@@', pairs, each

        for index, value in enumerate(pairs):
            pairs[index] = vests.get(value, value)

        if count == 2:
            result_set.update(pairs)
            results.append(tuple(pairs))
        elif count > 2:
            combs = list(itertools.combinations(pairs, 2))
            result_set.update(*combs)
            results.extend(combs)

    #pprint(result_set)
    #pprint(results)
    print len(results)

    with open('pairs.txt', 'w') as p:
        p.writelines([str(l) + os.linesep for l in results])
################################

################################

graph = results[::]


def draw_graph2(graph):
    # extract nodes from graph
    nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

    # create networkx graph
    G = nx.Graph()

    # add nodes
    for node in nodes:
        G.add_node(node)

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    import json
    import networkx as nx
    from networkx.readwrite import json_graph
    import http_server

    G = nx.barbell_graph(6,3)
    # this d3 example uses the name attribute for the mouse-hover value,
    # so add a name to each node
    for n in G:
        G.node[n]['name'] = n
    # write json formatted data
    d = json_graph.node_link_data(G) # node-link format to serialize
    # write json
    json.dump(d, open('force/force.json','w'))


    # draw graph
    #pos = nx.shell_layout(G)
    #nx.draw(G, pos)
    #show graph
    #plt.show()

# you may name your edge labels
#labels = map(chr, range(65, 65 + len(graph)))
#print labels
#draw_graph(graph, labels)

# if edge labels is not specified, numeric labels (0, 1, 2...) will be used
draw_graph(graph, graph_layout='spectral')
