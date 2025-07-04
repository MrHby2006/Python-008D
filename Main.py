from Funciones import guardar, mostrar, menu, buscar, eliminar

peliculas = []

cantidad = 0

while True:
    try:
        menu()
        opt = int(input("Ingrese la opción: "))
        if opt == 1:
            print("Guardar")
            guardar(peliculas)
            print("Pelicula guardada exitosamente")
        elif opt == 2:
            print("Mostrar")
            mostrar(peliculas)
        elif opt == 3:
            print("Eliminar")
            eliminar(peliculas)
        elif opt == 4:
            print("Buscar")
            buscar(peliculas)
        elif opt == 5:
            print("Salir")
            break
        else:
            print("Opción no valida")
    except ValueError:
        print("Solo se permiten valores numericos")
        
print("Gracias, vuelva pronto")