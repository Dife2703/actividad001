def suma_numeros():
    # Pedir al usuario que ingrese dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Sumar los dos números
    suma = num1 + num2

    # Mostrar el resultado
    print("La suma de", num1, "y", num2, "es:", suma)

# Llamar a la función para ejecutar el algoritmo
suma_numeros()