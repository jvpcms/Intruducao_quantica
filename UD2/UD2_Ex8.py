from matplotlib import pyplot as plt

a = [2, -1]
b = [1, 1]

c = [a[0] + b[0], a[1] + b[1]]
d = [a[0] - b[0], a[1] - b[1]]

plt.plot(a[0], a[1], 'ro')
plt.annotate("a = (2, -1)", a)

plt.plot(b[0], b[1], 'go')
plt.annotate("b = (1, 1)", b)

plt.plot(c[0], c[1], 'bo')
plt.annotate("a + b", c)

plt.plot(d[0], d[1], 'yo')
plt.annotate("a - b", d)

plt.plot(0, 0, 'ro')
plt.annotate("(0, 0)", [0, 0])

plt.show()
