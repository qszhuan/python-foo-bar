# -*- coding:utf-8 -*-
from optparse import OptionParser
import os
from os.path import basename

import matplotlib.pyplot as plt
import numpy as np


def autolabelh(rects):
    for rect in rects:
        width = rect.get_width()
        plt.text(width * 1.05, rect.get_y() + rect.get_height() / 2., '%d' % int(width),
                 ha='left', va='center', fontdict={'size': 10})


def generate(file_name, img_file_name):
    global data, headers, name_header, response_header, sorted_data, name, median_response_time, bar, title
    data = np.genfromtxt(fname=file_name, dtype=None, delimiter=',', names=True, comments=False, autostrip=True)
    headers = data.dtype.names
    name_header, response_header = headers[1], headers[4]
    sorted_data = np.sort(data, order=[response_header])
    name, median_response_time = sorted_data[name_header], sorted_data[response_header]
    bar = plt.barh(range(len(median_response_time)), median_response_time, align='edge', alpha=0.7)
    plt.yticks(range(len(name)), name, ha='right', va='bottom', size='small')
    plt.subplots_adjust(left=0.3)
    plt.grid(True)
    autolabelh(bar)
    title = os.linesep.join([basename(file_name), response_header.replace('_', ' ').upper()])
    plt.suptitle(title, fontsize=12, weight='bold')
    plt.savefig(img_file_name, bbox_inches='tight')


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="csv_file_name",
                      help="read data from csv file", metavar="FILE")

    (options, args) = parser.parse_args()
    img_file_name = '.'.join([options.csv_file_name, 'png'])
    generate(options.csv_file_name, img_file_name)
