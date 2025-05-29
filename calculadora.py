
print("Calculadora")
print("-------------------")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. o mayor Salir")
print("-------------------")

opcion = 0
valor_1 = 0
valor_2 = 0
resultado = 0

opcion = int(input("Ingrese la opción "))

while opcion < 5 and opcion > 0:
    if opcion == 1:
        print("Esta sumando")
        valor_1 = int(input("Ingrese el primer valor a sumar: "))
        valor_2 = int(input("Ingrese el segundo valor a sumar: "))
        resultado = valor_1 + valor_2
        print(f"El resultado de la suma es: {resultado}")
        print("-------------------")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. o mayor Salir")
        print("-------------------")
        opcion = int(input("Ingrese una opción: "))
    elif opcion == 2:
        print("Esta restando")
        valor_1 = int(input("Ingrese el primer valor a restar: "))
        valor_2 = int(input("Ingrese el segundo valor a restar: "))
        resultado = valor_1 - valor_2
        print(f"El resultado de la resta es: {resultado}")
        print("-------------------")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. o mayor Salir")
        print("-------------------")
        opcion = int(input("Ingrese una opción: "))
    elif opcion == 3:
        print("Esta multiplicando")
        valor_1 = int(input("Ingrese el primer valor a multiplicar: "))
        valor_2 = int(input("Ingrese el segundo valor a multiplicar: "))
        resultado = valor_1 * valor_2
        print(f"El resultado de la multiplicación es: {resultado}")
        print("-------------------")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. o mayor Salir")
        print("-------------------")
        opcion = int(input("Ingrese una opción: "))
    elif opcion == 4:
        print ("Esta dividiendo")
        valor_1 = int(input("Ingrese el dividendo: "))
        valor_2 = int(input("Ingrese el divisor: "))
        while valor_2 == 0:
            print("No se puede dividir por cero")
            valor_2 = int(input("Vueve a ingresar el divisor"))
        resultado = valor_1 / valor_2
        resultado_redondeado = round(resultado, 2)
        print(f"El resultado de la divición es: {resultado_redondeado}")
        print("-------------------")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. o mayor Salir")
        print("-------------------")
        opcion = int(input("Ingrese una opción: "))

print("Gracias, hasta luego")