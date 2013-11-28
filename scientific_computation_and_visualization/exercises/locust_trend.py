# -*- coding:utf-8 -*-
from itertools import groupby
from optparse import OptionParser
import numpy as np
import matplotlib.pyplot as plt


def generate(file_name, img_file_name):
    file_name = '/Users/zhuanqingshan/Dropbox/doc/graph/LOCUST02.2013-11-28.08.14.51.success.log.txt'
    img_file_name = file_name + '.png'

    data = np.genfromtxt(fname=file_name, dtype=None, delimiter='|', names=('time', '', '', '', 'name', 'response_time', ''),
                         comments=False, autostrip=True)

    sorted_data = np.sort(data, order=['name', 'time'])

    name_group = groupby(sorted_data['name'])
    name_list = list(name_group)
    
    print data['time'], data['name'], data['response_time']


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="csv_file_name",
                      help="read data from csv file", metavar="FILE")

    (options, args) = parser.parse_args()
    img_file_name = '.'.join([options.csv_file_name, 'png'])
    generate(options.csv_file_name, img_file_name)

