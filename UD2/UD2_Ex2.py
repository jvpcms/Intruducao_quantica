n = 0 + 1j

print(f"{n ** 2}")
print(f"{n ** 3}")
print(f"{n ** 4}")
print(f"{n ** 5}")


def i_to_a(a):
    if a % 4 == 0:
        print(n)
    elif a % 4 == 1:
        print(n ** 2)
    elif a % 4 == 2:
        print(n ** 3)
    else:
        print(n ** 4)


p = int(input("Power of i: "))

i_to_a(p)
