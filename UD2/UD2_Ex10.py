from math import atan, sqrt, pi

a = int(input("Coordenada X: "))
b = int(input("Coordenada Y: "))

print(f"R = {sqrt(a*a + b*b)}")
print(f"Teta = {atan(b/a)*180/pi}°")
