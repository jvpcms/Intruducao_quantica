import numpy as np
A = []
N = int(input("Insira dimensao de matriz: "))

for i in range(N):
    A.append([])
    for j in range(N):
        n = complex(input(f"Insira a{i + 1}{j + 1} na forma a+bj: "))
        A[i].append(n)

print("\nTranposta:\n")
print(np.matrix(A).transpose(), end='\n\n')
print("\nConjugada:\n")
print(np.matrix(A).conjugate(), end='\n\n')
print("\nDagger:\n")
print(np.matrix(A).transpose().conjugate())
