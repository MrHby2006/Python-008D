while True:
    
    try:
        numero = int(input("Ingrese el número: "))
        if numero % 2 == 0:
            print(f"Número {numero} es par")
        else:
            print(f"Número {numero} es impar")
    except ValueError:
        print("Debes ingresar un número valido")