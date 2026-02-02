C = float(input("Ingrese el capital inicial: "))
I = float(input("Ingrese el interés anual (0 a 100): "))
M = int(input("Ingrese la cantidad de años: "))

capital = C

for año in range(1, M + 1):
    capital += capital * (I / 100)
    print(f"Año {año}: capital = {capital:.2f}")

print(f"\nCapital final después de {M}")