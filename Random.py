
from random import randint

while True:
    n1 = int(input("Ingrese el primer número (Pulse 0 para salir): "))
    if n1 == 0:
        break
    n2 = int(input("Ingrese el segundo número (Pulse 0 para salir): "))
    if n2 == 0:
        break
        
    num = randint(n1,n2)
    print(f"El número aleatorio es: {num}")
    print("Vamos de nuevo")
    
print("Saliste, hasta luego")
    
# n1 = int(input("Ingrese el primer número: "))
# n2 = int(input("Ingrese el segundo número: "))

# num = randint(n1,n2)

# print(f"El número random es : {num}")