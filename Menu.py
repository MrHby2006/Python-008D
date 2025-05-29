print("Menú")
print("1. Primera opción")
print("2. Segunda opción")
print("3. Tercera opción")

opcion = int(input("Ingrese la opción: "))

while True:
    if opcion == 1:
        print("Primer nivel")
        print("Menú")
        print("1. Primera opción")
        print("2. Segunda opción")
        print("3. Tercera opción")
        opcion = int(input("Ingrese otra opción: "))
    elif opcion == 2:
        print("Menú")
        print("1. Primera opción")
        print("2. Segunda opción")
        print("3. Tercera opción")
        print("Segundo nivel")
        opcion = int(input("Ingrese otra opción: "))
    elif opcion == 3:
        print("Tercer nivel")
        break
    else:
        print("Opción no valida")
        print("Menú")
        print("1. Primera opción")
        print("2. Segunda opción")
        print("3. Tercera opción")
        opcion = int(input("Ingrese otra opción: "))