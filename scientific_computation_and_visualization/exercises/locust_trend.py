# -*- coding:utf-8 -*-
from datetime import datetime
from itertools import groupby
from matplotlib import dates
from matplotlib.ticker import NullFormatter
import numpy as np
import matplotlib.pyplot as plt


time_convert_func = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S,%f')


class LocustTrend(object):
    def __init__(self, filename, seperated=False):
        self.filename = filename
        self.seperated = seperated

        self.hfmt = dates.DateFormatter('%m/%d %H:%M')

        headers = ['time', 'label', 'loglevel', 'method', 'name', 'response_time', 'size']
        dtype = [(headers[0], 'object')] + [(col, '|S128') for col in headers[1:-2]] + [(col, 'i') for col in
                                                                                        headers[-2:]]
        self.data = np.genfromtxt(fname=file_name,
                                  delimiter='|',
                                  autostrip=True,
                                  dtype=dtype,
                                  names=headers,
                                  converters={'time': time_convert_func})
        self.sorted_data = np.sort(self.data, order=['name', 'time'])
        self.grouped_name = groupby(self.sorted_data['name'])
        self.requests_counts = np.array([[key, len(list(group))] for key, group in self.grouped_name])
        self.time_distribution = self.time_dist_func(self.data['time'])
        self._init_graph_rect()

    def time_dist_func(self, data):
        return [t.hour * 60 + t.minute for t in data]

    def _set_basic_graph(self):
        self.ax_plot = plt.axes(self.rect_scatter)
        plt.xticks(rotation='vertical')
        self.ax_hist_x = plt.axes(self.rect_histx)
        self.ax_hist_y = plt.axes(self.rect_histy)
        self.ax_plot.xaxis.set_ticks(range(self.time_distribution[0], self.time_distribution[-1], 10))

        self.ax_plot.xaxis.set_major_locator(dates.MinuteLocator(interval=5))
        self.ax_plot.xaxis.set_major_formatter(self.hfmt)
        self.ax_plot.figure.set_size_inches(16, 12)
        self.ax_plot.set_ylabel('Response Time(ms)')

        self.ax_plot.grid(True)
        self.ax_hist_x.grid(True)
        self.ax_hist_y.grid(True)

        # no labels
        null_fmt = NullFormatter()         # no labels
        self.ax_hist_x.xaxis.set_major_formatter(null_fmt)
        self.ax_hist_y.yaxis.set_major_formatter(null_fmt)
        self.ax_hist_x.set_ylabel('Request Count')
        self.ax_hist_y.set_xlabel('Request Count')

        self.ax_hist_x.xaxis.set_ticks(range(self.time_distribution[0], self.time_distribution[-1], 10))


    def generate(self):
        self._set_basic_graph()

        start_index = 0
        for index, request in enumerate(self.requests_counts):
            name, count = request[0], int(request[1])
            if name != 'HomePage-offices':
                start_index += count
                continue

            end_index = start_index + count
            self.ax_plot.plot(self.sorted_data['time'][start_index:end_index],
                              self.sorted_data['response_time'][start_index:end_index],
                              'o')
            if self.seperated:
                self.ax_hist_x.hist([t.hour * 60 + t.minute for t in self.sorted_data['time'][start_index:end_index]])
                time_distribution = self.time_dist_func(self.sorted_data['time'][start_index:end_index])
                print time_distribution
                self.ax_hist_x.xaxis.set_ticks()

                self.ax_hist_y.hist(self.sorted_data['response_time'][start_index:end_index], orientation='horizontal', bins=10)

                plt.sca(self.ax_hist_x)
                plt.title('\n'.join([self.filename, name]), fontsize=24)
                img_file_name = '.'.join([self.filename, name, 'png'])
                plt.savefig(img_file_name, dpi=100, bbox_inchs='tight')
                plt.clf()
                self._set_basic_graph()
            start_index += count

        if not self.seperated:
            self.ax_hist_x.hist([t.hour * 60 + t.minute for t in self.data['time']], bins=60)
            self.ax_hist_y.hist(self.data['response_time'], orientation='horizontal', bins=10)

            plt.sca(self.ax_hist_x)
            plt.title('\n'.join([self.filename, 'Overview']), fontsize=24)
            img_file_name = '.'.join([self.filename, 'png'])
            plt.savefig(img_file_name, dpi=100, bbox_inches='tight')

    def _init_graph_rect(self):
        left, width = 0.1, 0.65
        bottom, height = 0.1, 0.65
        bottom_h = left_h = left + width + 0.02

        self.rect_scatter = [left, bottom, width, height]
        self.rect_histx = [left, bottom_h, width, 0.2]
        self.rect_histy = [left_h, bottom, 0.2, height]


if __name__ == '__main__':
    #parser = OptionParser()
    #parser.add_option("-s", "--source", dest="csv_file_name",
    #                  help="read data from csv file", metavar="FILE")
    #
    #(options, args) = parser.parse_args()
    #file_name, img_file_name = options.csv_file_name, '.'.join([options.csv_file_name, 'png'])
    file_name = r'/Users/zhuanqingshan/Dropbox/doc/graph/LOCUST02.2013-11-28.08.14.51.success.log.txt'
    img_file_name = '.'.join([file_name, 'png'])

    LocustTrend(file_name, seperated=True).generate()
