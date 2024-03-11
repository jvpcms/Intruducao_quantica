from matplotlib import pyplot as plt

cr = float(input("Parte real de c: "))
ci = float(input("Parte imaginaria de c: "))
r = float(input("r0: "))
i = float(input("i0: "))

a = [cr*r, ci*r]
b = [(-1)*a[1], a[0]]

plt.plot(a[0], a[1], 'ro')
plt.annotate("c * r0", a)
plt.plot(b[0], b[1], 'ro')
plt.annotate("c * i0", b)

plt.axis('equal')
plt.grid()

plt.show()
