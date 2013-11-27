# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0, 5, 0.2)
t2 = np.arange(0, 5, 0.1)

plt.figure(1)
plt.subplot(221)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(222)
plt.plot(t2, np.cos(t2*2*np.pi), 'r--')

plt.subplot(4, 4, 16)
plt.plot(t1, t1, 'g*')

plt.savefig('lesson3.png')
plt.show()


