import math

x = float(input("Ingrese el valor de x: "))
n = int(input("Ingrese el número de términos n: "))

resultado = 0
for i in range(n + 1):
    resultado += (x ** i) / math.factorial(i)

print(f"Aproximación de e {x} usando {n} términos: {resultado}")