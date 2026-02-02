def invertir_numero(n):
    invertido = 0

    while n > 0:
        digito = n % 10       
        invertido = invertido * 10 + digito
        n = n // 10             

    return invertido

numero = 37368
resultado = invertir_numero(numero)
print(resultado)  