import random

def estimar_pi(N):
    puntos_dentro = 0

    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            puntos_dentro += 1

    pi_aproximado = 4 * puntos_dentro / N
    return puntos_dentro, pi_aproximado

N = random.randint(1,10000)

puntos_dentro, pi_estimado = estimar_pi(N)

print("\nResultados de la simulación:"f"\nNúmero total de generados: {N}"f"\nNúmero de puntos dentro del círculo: {puntos_dentro}"f"\nValor aproximado de π: {pi_estimado}")