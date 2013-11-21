# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4]
y = np.arange(1, 3, 0.5)                 # why use different method with x to get y: for ** operation
plt.plot(x, y, 'go-', x, y ** 2, 'r+-')  # plot two lines
lines = plt.plot(x, y ** 3, ':', linewidth=2, color='c')     # set line properties with arbitrary attr
line, = plt.plot(x, y ** 4)               # get line generated.
plt.setp(line, 'linewidth', 2)          # method to set line properties

plt.axis([0, 5, 0, 50])
plt.show()


