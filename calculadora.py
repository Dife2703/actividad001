def calculadora():
    # Pedir al usuario que ingrese dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Pedir al usuario que ingrese la operación deseada
    operacion = input("Ingrese la operación a realizar (+, -, *, /): ")

    # Realizar la operación deseada y mostrar el resultado
    if operacion == '+':
        resultado = num1 + num2
        print("La suma de", num1, "y", num2, "es:", resultado)
    elif operacion == '-':
        resultado = num1 - num2
        print("La resta de", num1, "y", num2, "es:", resultado)
    elif operacion == '*':
        resultado = num1 * num2
        print("La multiplicación de", num1, "y", num2, "es:", resultado)
    elif operacion == '/':
        if num2 != 0:  # Para evitar división por cero
            resultado = num1 / num2
            print("La división de", num1, "entre", num2, "es:", resultado)
        else:
            print("Error: No se puede dividir entre cero.")
    else:
        print("Operación no válida.")

# Llamar a la función para ejecutar la calculadora
calculadora()