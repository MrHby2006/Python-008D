
suma = 0

while True:
    numero = int(input("Introduce un número (Negativo para terminar): "))
   if numero < 0:
       break
   suma += numero
   
print(f"La suma de los números positivos es: {suma}") 