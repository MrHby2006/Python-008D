
num_ingresado = int(input("Ingrese un número a sumar:"))

negativo = False
resultado = 0

while not negativo:
    if num_ingresado < 0:
        negativo = True
        break
    resultado = resultado + num_ingresado
    print(f"El resultado es: {resultado}")
    num_ingresado = int(input("Ingrese un número a sumar:"))
