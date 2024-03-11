from matplotlib import pyplot as plt

cr = float(input("Parte real de c: "))
ci = float(input("Parte imaginaria de c: "))

a = [cr]
b = [ci]

for i in range(9):
    a.append(cr)
    b.append(b[i] + 1)

plt.plot(a, b, 'ro')

plt.axis('equal')
plt.grid()

plt.show()
