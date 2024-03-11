from matplotlib import pyplot as plt
from math import atan, sqrt


def r(x, y):
    return sqrt(x*x + y*y)


def teta(x, y):
    return atan(y/x)


a = [2, -1]
b = [1, 1]

c = [a[0] + b[0], a[1] + b[1]]
d = [a[0] - b[0], a[1] - b[1]]

R = [r(a[0], a[1]), r(b[0], b[1]), r(c[0], c[1]), r(d[0], d[1])]
Teta = [teta(a[0], a[1]), teta(b[0], b[1]), teta(c[0], c[1]), teta(d[0], d[1])]

fig = plt.figure(dpi=200)
ax = fig.add_subplot(projection='polar')

plt.polar(Teta[0], R[0], marker='o')
plt.polar(Teta[1], R[1], marker='o')
plt.polar(Teta[2], R[2], marker='o')
plt.polar(Teta[3], R[3], marker='o')

ax.set_ylim(0, 10)
plt.show()
