texto = input("Ingresa una cadena de 50 caracteres: ")

while len(texto) != 50:
    texto = input("Debe tener exactamente 50 caracteres. Intenta de nuevo: ")

cantidad_a = texto.count('a')

print("La letra 'a' se repite", cantidad_a, "veces.")