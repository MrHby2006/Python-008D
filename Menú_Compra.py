saldo = 1_000_000
simulacion = 0

print("Tienda Falabella")
print("Que es lo que quiere hacer?")
print("1. Comprar")
print("2. Ver los articuulos que lleva")
print("3. Salir")

opcion = int(input("Elija una opción: "))

while True:
    if opcion == 1:
        print("Va a comprar")
        
    elif opcion == 2:
        print("Simulación de compras")
        llevar = int(input("Ingrese el precio del articulo que le gustaria llevar (pulse 0 para terminar): "))
        if llevar == 0:
            print(f"La simulación dice que gataria ${simulacion} pesos")
        else:
            simulacion = simulacion + llevar
    elif opcion == 3:
        print("Chao, que tenga un buen día")
        break