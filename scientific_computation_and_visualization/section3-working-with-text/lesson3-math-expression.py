# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

plt.title('alpha > beta')

plt.text(0, 0, r'$\alpha > \beta$', fontsize=20, weight='bold')
plt.text(0, 0.2, r'$\alpha_i > \beta_i$', fontsize=20, weight='bold')
plt.text(0, 0.4, r'$\sum_{i=0}^\infty x_i$', fontsize=20, weight='bold')
plt.text(0, 0.6, r'$\frac{3}{4} \binom{5}{6} \stackrel{3}{4}$', fontsize=20, weight='bold')
plt.text(0, 0.8, r'$\frac{3}{4} \binom{5}{6} \stackrel{3}{4}$', fontsize=20, weight='bold')
plt.text(0.2, 0, r'$\frac{5-\frac{1}{x}}{4}$', fontsize=20, weight='bold')
plt.text(0.2, 0.2, r'$(\frac{5-\frac{1}{x}}{4})$', fontsize=20, weight='bold')
plt.text(0.2, 0.4, r'$\left(\frac{5-\frac{1}{x}}{4}\right)$', fontsize=20, weight='bold')
plt.text(0.2, 0.6, r'$\sqrt{2}$', fontsize=20, weight='bold')
plt.text(0.2, 0.8, r'$\sqrt[3]{x}$', fontsize=20, weight='bold')
plt.text(0.4, 0, r'$s(t) = \mathcal{A}\cdot\sin(2 \omega t)$', fontsize=20, weight='bold')

plt.savefig('math-expression.jpg')

plt.show()