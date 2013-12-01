# -*- coding:utf-8 -*-
from datetime import datetime
from itertools import groupby
from matplotlib import dates
from matplotlib.ticker import NullFormatter
import numpy as np
import matplotlib.pyplot as plt


#def time_convert_func(str):
#    return datetime.strptime(str, '%Y-%m-%d %H:%M:%S,%f')

time_convert_func = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S,%f')


def set_xaxis(ax_plot):
    hfmt = dates.DateFormatter('%m/%d %H:%M')
    ax_plot.xaxis.set_major_locator(dates.MinuteLocator(interval=5))
    ax_plot.xaxis.set_major_formatter(hfmt)


def generate(file_name, img_file_name, seperated=False):
    headers = ['time', 'label', 'loglevel', 'method', 'name', 'response_time', 'size']
    dtype = [(headers[0], 'object')] + [(col, '|S128') for col in headers[1:-2]] + [(col, 'i') for col in headers[-2:]]
    data = np.genfromtxt(fname=file_name,
                         delimiter='|',
                         autostrip=True,
                         dtype=dtype,
                         names=headers,
                         converters={'time': time_convert_func})

    sorted_data = np.sort(data, order=['name', 'time'])
    grouped_name = groupby(sorted_data['name'])
    requests_counts = np.array([[key, len(list(group))] for key, group in grouped_name])
    #slow_request_names = set([i['name'] for i in data if i['response_time'] >35000])

    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left + width + 0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]

    ax_plot = plt.axes(rect_scatter)
    plt.xticks(rotation='vertical')
    set_xaxis(ax_plot)
    ax_plot.figure.set_size_inches(16, 12)
    ax_plot.set_ylabel('Response Time(ms)')
    ax_plot.grid(True)

    ax_hist_x = plt.axes(rect_histx)
    ax_hist_x.grid(True)
    ax_hist_y = plt.axes(rect_histy)
    ax_hist_y.grid(True)

    # no labels
    null_fmt = NullFormatter()         # no labels
    ax_hist_x.xaxis.set_major_formatter(null_fmt)
    ax_hist_y.yaxis.set_major_formatter(null_fmt)

    time_distribution = [t.hour * 60 + t.minute for t in data['time']]
    ax_hist_x.xaxis.set_ticks(range(time_distribution[0], time_distribution[-1], 10))
    ax_hist_x.hist([t.hour * 60 + t.minute for t in data['time']], bins=60)
    ax_hist_x.set_ylabel('Request Count')
    ax_hist_y.hist(data['response_time'], orientation='horizontal', bins=10)
    ax_hist_y.set_xlabel('Request Count')

    start_index = 0
    for index, request in enumerate(requests_counts):
        name, count = request
        count = int(count)
        #if name not in slow_request_names:
        #    start_index += count
        #    continue
        end_index = start_index + count
        ax_plot.plot(sorted_data['time'][start_index:end_index],
                     sorted_data['response_time'][start_index:end_index],
                     'o')
        start_index += count

        if seperated:
            plt.suptitle('\n'.join([file_name, name]))
            img_file_name = '.'.join([file_name, name, 'png'])
            plt.savefig(img_file_name, dpi=100)
            plt.clf()

    if not seperated:
        plt.suptitle('Overview')

        plt.savefig(img_file_name, dpi=100, bbox_inches='tight')


if __name__ == '__main__':
    #parser = OptionParser()
    #parser.add_option("-s", "--source", dest="csv_file_name",
    #                  help="read data from csv file", metavar="FILE")
    #
    #(options, args) = parser.parse_args()
    #file_name, img_file_name = options.csv_file_name, '.'.join([options.csv_file_name, 'png'])
    file_name = r'/Users/zhuanqingshan/Dropbox/doc/graph/LOCUST02.2013-11-28.08.14.51.success.log.txt'
    img_file_name = '.'.join([file_name, 'png'])
    generate(file_name=file_name, img_file_name=img_file_name, seperated=False)
