limite = 1000

es_primo = [True] * (limite + 1)

es_primo[0] = False
es_primo[1] = False

for numero in range(2, int(limite ** 0.5) + 1):
    if es_primo[numero]:
        for multiplo in range(numero * numero, limite + 1, numero):
            es_primo[multiplo] = False

primos = [i for i in range(2, limite + 1) if es_primo[i]]

print("Números primos entre 1 y 1000:")
print(primos)
print("\nCantidad de números primos:", len(primos))