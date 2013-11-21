# -*- coding:utf-8 -*-


import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
plt.plot(x)                             # create a linear chart with y-axis range: [1,2,3,4], x-axis is default:[0,1,2,3]
plt.ylabel('some numbers')              # set xlabel
plt.xlabel('x label')                   # set ylabel
plt.title('Advance pyplot')             # set title
plt.axis([0, 20, 0, 16])                # set x-axis and y-axis range


plt.show()


