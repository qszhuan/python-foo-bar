# -*- coding:utf-8 -*-

import matplotlib

file_path = matplotlib.matplotlib_fname()
print file_path
#
#with open(file_path) as f:
#    for line in f.readlines():
#        if not line.startswith('# '):
#            print line

#print matplotlib.rcParams

print matplotlib.rcParams['lines.linewidth']

matplotlib.rc('lines', linewidth=2, color='r')

matplotlib.rcdefaults()


