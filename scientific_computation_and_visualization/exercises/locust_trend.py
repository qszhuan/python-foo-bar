# -*- coding:utf-8 -*-
from datetime import datetime
from itertools import groupby
from optparse import OptionParser
import numpy as np
import matplotlib.pyplot as plt


def time_convert_func(str):
    return datetime.strptime(str, '%Y-%m-%d %H:%M:%S,%f')


def generate(file_name, img_file_name):
    #file_name = r'C:\perf-test-results\11-28-17.20\LOCUST02.2013-11-28.08.14.51.success.log.txt'
    file_name = r'/Users/zhuanqingshan/Dropbox/doc/graph/LOCUST02.2013-11-28.08.14.52.success.log.txt'
    img_file_name = file_name + '.png'

    time_convert_func = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S,%f')

    headers = ['time', 'label', 'loglevel', 'method', 'name', 'response_time', 'size']
    dtype = [(headers[0], 'object')] + [(col, '|S32') for col in headers[1:-2]] + [(col, 'i') for col in headers[-2:]]
    data = np.genfromtxt(fname=file_name,
                         delimiter='|',
                         autostrip=True,
                         dtype=dtype,
                         names=headers,
                         converters={'time': time_convert_func})

    sorted_data = np.sort(data, order=['name', 'time'])

    grouped_name = groupby(sorted_data['name'])

    requests_counts = np.array([[key, len(list(group))] for key, group in grouped_name])

    lens = len(requests_counts)
    start_index = 0
    plt.grid(True)
    for index, request in enumerate(requests_counts):
        name, count = request
        count = int(count)
        #plt.subplot(1, 1, 11)
        #plt.title(request[0])
        yaxis = sorted_data['response_time'][start_index:start_index + count]
        xaxis = sorted_data['time'][start_index:start_index + count]
        plt.plot(xaxis, yaxis, 'o')
        start_index += count

    plt.legend(requests_counts[:,0])
    plt.savefig(file_name + '.'+name + '.png', dpi=1024)
    #plt.clf()

    print data['time'], data['name'], data['response_time']


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="csv_file_name",
                      help="read data from csv file", metavar="FILE")

    (options, args) = parser.parse_args()
    img_file_name = '.'.join([options.csv_file_name, 'png'])
    generate(options.csv_file_name, img_file_name)
