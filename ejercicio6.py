mayor_sueldo = 0
orden_mayor = 0
contador = 0
suma_sueldos = 0

while True:
    orden = int(input("Ingrese el número de orden del empleado: "))
    sueldo = float(input("Ingrese el sueldo del empleado (0 o negativo para terminar): "))

    if sueldo <= 0:
        break

    contador += 1
    suma_sueldos += sueldo

    if sueldo > mayor_sueldo:
        mayor_sueldo = sueldo
        orden_mayor = orden

if contador > 0:
    promedio = suma_sueldos / contador
    print("\nEmpleado con mayor sueldo:")
    print("Número de orden:", orden_mayor)
    print("Mayor sueldo:", mayor_sueldo)
    print("\nCantidad de sueldos ingresados:", contador)
    print("Promedio de sueldos:", promedio)
else:
    print("No se ingresaron sueldos válidos.")
