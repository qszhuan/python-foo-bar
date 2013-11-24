# -*- coding:utf-8 -*-


import matplotlib.pyplot as plt
import matplotlib.patches as patches

left, width = 0.25, 0.5
bottom, height = 0.25, 0.5
right = left + width
top = bottom + height

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

p = patches.Rectangle((left, bottom),
                      width, height,
                      fill=False,
                      transform=ax.transAxes,
                      clip_on=False)

ax.text(left, top, 'left top',
        horizontalalignment='left',
        verticalalignment='top',
        transform=ax.transAxes)

ax.text(left, bottom, 'left bottom',
        horizontalalignment='left',
        verticalalignment='bottom',
        transform=ax.transAxes)

ax.add_patch(p)
plt.show()
