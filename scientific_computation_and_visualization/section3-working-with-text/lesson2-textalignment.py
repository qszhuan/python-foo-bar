# -*- coding:utf-8 -*-


import matplotlib.pyplot as plt
import matplotlib.patches as patches

left, width = 0.25, 0.5
bottom, height = 0.25, 0.5
right = left + width
top = bottom + height

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
line, = plt.plot([1, 2, 3, 4])

p = patches.Rectangle((left, bottom),
                      width, height,
                      fill=False,
                      transform=ax.transAxes,
                      clip_on=False)

t1 = ax.text(left, bottom, 'left top',
             horizontalalignment='left',
             verticalalignment='top',
             transform=ax.transAxes)

t2 = ax.text(left, bottom, 'left bottom',
             horizontalalignment='left',
             verticalalignment='bottom',
             transform=ax.transAxes)

t3 = ax.text(right, top, 'right bottom',
             horizontalalignment='right',
             verticalalignment='bottom',
             transform=ax.transAxes)

t4 = ax.text(right, top, 'right top',
             horizontalalignment='right',
             verticalalignment='top',
             transform=ax.transAxes)

t5 = ax.text(right, bottom, 'center top',
             horizontalalignment='center',
             verticalalignment='top',
             transform=ax.transAxes)

t6 = ax.text(left, 0.5 * (bottom + top), 'right center',
             horizontalalignment='right',
             verticalalignment='center',
             transform=ax.transAxes,
             bbox=dict(facecolor='red', alpha=0.5))

t7 = ax.text(left, 0.5 * (bottom + top), 'right center vertical rotation',
             horizontalalignment='right',
             verticalalignment='center',
             rotation='vertical',
             transform=ax.transAxes,
             bbox=dict(facecolor='green', alpha=0.5))

t8 = ax.text(left, 0.5 * (bottom + top), 'left center',
             horizontalalignment='left',
             verticalalignment='center',
             transform=ax.transAxes,
             bbox=dict(facecolor='blue', alpha=0.5))

t9 = ax.text(left, 0.5 * (bottom + top), 'left center vertical rotation',
             horizontalalignment='left',
             verticalalignment='center',
             transform=ax.transAxes,
             rotation='vertical',
             bbox=dict(facecolor='yellow', alpha=0.5))

t10 = ax.text(0.5 * (left + right), 0.5 * (bottom + top), 'middle',
              horizontalalignment='center',
              verticalalignment='center',
              fontsize=20,
              color='red')

t11 = ax.text(right, 0.5 * (bottom + top), 'centered',
              horizontalalignment='center',
              verticalalignment='center',
              rotation='vertical',
              transform=ax.transAxes,
              bbox=dict(color='yellow', facecolor='blue', alpha=0.5))

t12 = ax.text(left, top, 'rotated\n with newlines',
              horizontalalignment='center',
              verticalalignment='center',
              rotation=45,
              transform=ax.transAxes,
              weight='bold',
              bbox=dict(facecolor='red', alpha=0.5))

t13 = ax.text(left, top, 'no rotation\n with newlines', horizontalalignment='center',
              verticalalignment='center',
              transform=ax.transAxes,
              style='italic',
              bbox=dict(facecolor='green', alpha=0.5))

objs = (ax, p, line, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13)
print [each.get_zorder() for each in objs]
ax.add_patch(p)
plt.show()
