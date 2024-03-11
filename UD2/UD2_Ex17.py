import numpy as np

A = []
B = []
N = int(input("Insira dimensao de matriz: "))

for i in range(N):
    A.append([])
    for j in range(N):
        n = complex(input(f"Insira a{i + 1}{j + 1} da forma a+bj: "))
        A[i].append(n)

for i in range(N):
    B.append([])
    for j in range(N):
        n = complex(input(f"Insira b{i + 1}{j + 1} da forma a+bj: "))
        B[i].append(n)

print("\nProduto interno:\n")
print(np.dot(np.matrix(A), np.matrix(B)))
