import random

numero_secreto = random.randint(1, 10)

intento = 1
sigue_jugando = True

intento_ingresado = int(input("Ingrese su primer intento: "))
if intento_ingresado == numero_secreto:
    print(f"Felicitaciones, has ganado en {intento} intento")
    sigue_jugando = False
elif intento_ingresado > numero_secreto:
    print("El número ingresado es mayor al número secreto")
    intento = intento + 1
else:
    print("El número ingresado es menor al número secreto")
    intento = intento + 1 
if sigue_jugando:
    intento_ingresado = int(input("Ingrese su segundo intento: "))
    if(intento_ingresado == numero_secreto):
        print(f"Felicitaciones, has ganado en {intento} intentos")
        sigue_jugando = False
    elif intento_ingresado > numero_secreto:
        print("El número ingresado es mayor al número secreto")
        intento = intento + 1
    else:
        print("El número ingresado es menor al número secreto")
        intento = intento + 1        
if sigue_jugando:
    intento_ingresado = int(input("Ingrese su tercer intento: "))
    if(intento_ingresado == numero_secreto):
        print(f"Felicitaciones, has ganado en {intento} intentos")
        sigue_jugando = False
    elif intento_ingresado > numero_secreto:
        print("El número ingresado es mayor al número secreto")
        intento = intento + 1
    elif intento_ingresado < numero_secreto:
        print("El número ingresado es menor al número secreto")
        intento = intento + 1   

print("Te quedaste sin turnos")
print(f"El número secreto es {numero_secreto}")     
print("Gracias por jugar")