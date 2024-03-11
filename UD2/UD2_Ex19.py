import numpy as np

A = []
N = int(input("Insira dimensao de matriz: "))

for i in range(N):
    A.append([])
    for j in range(N):
        n = complex(input(f"Insira a{i + 1}{j + 1} da forma a+bj: "))
        A[i].append(n)

print("\nTransposta:\n")
print(np.matrix(A).transpose())

print("\nConjugada:\n")
print(np.matrix(A).conjugate())

if np.array_equal(np.matrix(A).transpose(), np.matrix(A).conjugate()):
    print("Hermitiana")
else:
    print("Nao hermitiana")
