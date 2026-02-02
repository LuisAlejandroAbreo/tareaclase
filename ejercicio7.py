import random

numero_secreto = random.randint(1, 1000)

intentos_maximos = 10
intentos = 0
adivinado = False

print("He pensado un número entero entre 1 y 1000.")
print("Tienes 10 intentos para adivinarlo.\n")

while intentos < intentos_maximos and not adivinado:
    intento = int(input(f"Intento {intentos + 1}: Ingresa un número: "))
    intentos += 1

    if intento < numero_secreto:
        print("El número a adivinar es MAYOR.\n")
    elif intento > numero_secreto:
        print("El número a adivinar es MENOR.\n")
    else:
        adivinado = True
        print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")

if not adivinado:
    print(f"\nSe han agotado los intentos." f"\nEl número secreto era: {numero_secreto}")