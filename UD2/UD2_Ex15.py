from numpy.linalg import inv

A = []
B = []
C = []
k = float(input("Insira escalar k: "))
N = int(input("Insira dimensao de matriz: "))

for i in range(N):
    A.append([])
    for j in range(N):
        n = float(input(f"Insira a{i + 1}{j + 1}: "))
        A[i].append(n)

for i in range(N):
    B.append([])
    for j in range(N):
        n = float(input(f"Insira b{i + 1}{j + 1}: "))
        B[i].append(n)

print("\nA + B\n")

for i in range(N):
    C.append([])
    for j in range(N):
        C[i].append(A[i][j] + B[i][j])

print(C)

print("\nA^-1\n")
print(inv(A))

print("\nB^-1\n")
print(inv(B))

print("\nA x k\n")

for i in range(N):
    for j in range(N):
        A[i][j] *= k

print(A)
