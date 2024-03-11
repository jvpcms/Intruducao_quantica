A = []
B = []
N = int(input("Insira dimensao de vetor A: "))

for i in range(N):
    A.append(complex(input(f"Insira a{i + 1} da forma a+bj: ")))

M = int(input("\nInsira dimensao de vetor B: "))

for i in range(M):
    B.append(complex(input(f"Insira b{i + 1} da forma a+bj: ")))

C = []

for i in range(N):
    for j in range(M):
        C.append(A[i]*B[j])

print(f"\n{C}")
