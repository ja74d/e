#/usr/bin/python3.8

import matplotlib.pyplot as plt
import numpy as np


x = []

for i in range(-10, 11):
    x.append(i)

y = []

for j in x:
    w = 2*j
    y.append(w)


xprime = []
for k in range(-10, 11):
    xprime.append(k)

yprime = []
for l in xprime:
    h = 3*l + 2
    yprime.append(h)


# Add grid lines
plt.grid(True, linestyle='--', alpha=0.5)

# Customize axis labels
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)


plt.plot(x, y)
plt.plot(xprime, yprime)
plt.show()