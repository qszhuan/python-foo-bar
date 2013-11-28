# -*- coding:utf-8 -*-
import os
from os.path import basename

import matplotlib.pyplot as plt
import numpy as np
filename = '/Users/zhuanqingshan/Dropbox/doc/graph/2013-11-28_08_24_51_250_requests.csv'


def autolabelh(rects):
    for rect in rects:
        width = rect.get_width()
        plt.text(width * 1.05, rect.get_y() + rect.get_height() / 2., '%d' % int(width),
                 ha='left', va='center', fontdict={'size': 10})


data = np.genfromtxt(fname=filename, dtype=None, delimiter=',', names=True, comments=False, autostrip=True)

headers = data.dtype.names
name_header, response_header = headers[1], headers[4]
sorted_data = np.sort(data, order=[response_header])
name, median_response_time = sorted_data[name_header], sorted_data[response_header]

bar = plt.barh(range(len(median_response_time)), median_response_time, align='edge', alpha=0.7)
plt.yticks(range(len(name)), name, ha='right', va='bottom', size='small')

plt.subplots_adjust(left=0.3)
plt.grid(True)
autolabelh(bar)

title = os.linesep.join([basename(filename), response_header.replace('_', ' ').upper()])
plt.suptitle(title, fontsize=12, weight='bold')
plt.savefig('requests.png', bbox_inches='tight')

plt.show()
