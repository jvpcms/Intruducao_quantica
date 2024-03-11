from matplotlib import pyplot as plt

cr = float(input("Parte real de c: "))
ci = float(input("Parte imaginaria de c: "))

a = [cr]
b = [ci]

for i in range(9):
    a.append(a[i]*cr - b[i]*ci)
    b.append(b[i]*cr + a[i]*ci)

plt.plot(a, b, 'ro')

plt.axis('equal')
plt.grid()

print("A cada operacao, o modulo do numero se multiplica e o angulo se soma")

plt.show()
