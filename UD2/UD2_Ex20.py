import numpy as np
A = []
N = int(input("Insira dimensao de matriz: "))

for i in range(N):
    A.append([])
    for j in range(N):
        n = complex(input(f"Insira a{i + 1}{j + 1} na forma a+bj: "))
        A[i].append(n)

B = np.matrix(A).transpose().conjugate()
print("\nDagger:\n")
print(B)

if np.array_equal(np.matmul(A, B), np.matmul(B, A)):
    print("Unitaria")
else:
    print("Nao Unitaria")
