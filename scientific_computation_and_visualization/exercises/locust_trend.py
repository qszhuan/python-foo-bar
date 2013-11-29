# -*- coding:utf-8 -*-
from itertools import groupby
from optparse import OptionParser
import numpy as np
import matplotlib.pyplot as plt


def generate(file_name, img_file_name):
    file_name = r'C:\perf-test-results\11-28-17.20\LOCUST02.2013-11-28.08.14.51.success.log.txt'
    img_file_name = file_name + '.png'

    data = np.genfromtxt(fname=file_name, dtype=None, delimiter='|', names=('time', '', '', '', 'name', 'response_time', ''),
                         comments=False, autostrip=True)

    sorted_data = np.sort(data, order=['name', 'time'])

    grouped_name = groupby(sorted_data['name'])

    requests_counts = [[key, len(list(group))] for key, group in grouped_name]

    lens = len(requests_counts)
    start_index = 0
    for index, request in enumerate(requests_counts):
        if index>2:
            break
        name, count = request
        #plt.subplot(1, 1, 11)
        #plt.title(request[0])
        yaxis = sorted_data['response_time'][start_index:start_index + count]
        plt.plot(range(len(yaxis)), yaxis)
        start_index += count

    xtime = len(set(data['time']))
    plt.xlabel([0, xtime, 0, 50000])



    print data['time'], data['name'], data['response_time']


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="csv_file_name",
                      help="read data from csv file", metavar="FILE")

    (options, args) = parser.parse_args()
    img_file_name = '.'.join([options.csv_file_name, 'png'])
    generate(options.csv_file_name, img_file_name)
