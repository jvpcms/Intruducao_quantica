a = complex(input("Complex number 1: "))
b = complex(input("Complex number 2: "))

print(f"\nconj(a) + conj(b) = {a.conjugate() + b.conjugate()}")
print(f"conj(a + b) = {(a + b).conjugate()}\n")

print(f"conj(a) * conj(b) = {a.conjugate() * b.conjugate()}")
print(f"conj(a * b) = {(a * b).conjugate()}")
