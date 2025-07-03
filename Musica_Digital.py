albums = {
    "ALB001": ["a night at the opera", "queen", "rock", 1975, "vinilo"],
    "ALB002": ["thriller", "michael jackson", "pop", 1982, "cd"],
    "ALB003": ["dark side of the moon", "pink floyd", "rock", 1973, "vinilo"],
    "ALB004": ["21", "adele", "pop", 2011, "digital"],
    "ALB005": ["abbey road", "the beatles", "rock", 1969, "vinilo"],
    "ALB006": ["back in black", "ac/dc", "rock", 1980, "cd"],
    "ALB007": ["the wall", "pink floyd", "rock", 1979, "cd"],
    "ALB008": ["lemonade", "beyoncé", "r&b", 2016, "digital"]
}

inventario = {
    "ALB001": [6],
    "ALB002": [7],
    "ALB003": [8],
    "ALB004": [9],
    "ALB005": [10],
    "ALB006": [0],
    "ALB007": [11],
    "ALB008": [12]
}

def menu():
    while True:
        print("\n*** MENÚ PRINCIPAL ***")
        print("1. Stock por Género.")
        print("2. Búsqueda por Año de Lanzamiento.")
        print("3. Actualizar Cantidad de Stock.")
        print("4. Salir.")

        opcion = input("Ingrese opción: ")

        if opcion == "1":
            genero = input("Ingrese género a consultar: ")
            stock_genero(genero)

        elif opcion == "2":
            while True:
                try:
                    anio_min = int(input("Ingrese año mínimo: "))
                    anio_max = int(input("Ingrese año máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            busqueda_anio(anio_min, anio_max)

        elif opcion == "3":
            while True:
                album_id = input("Ingrese ID de álbum a actualizar: ").strip()
                try:
                    nueva_cantidad = int(input("Ingrese nueva cantidad: "))
                except ValueError:
                    print("Debe ingresar un número entero para el stock.")
                    continue

                resultado = actualizar_stock(album_id, nueva_cantidad)
                if resultado:
                    print("Stock actualizado!!")
                else:
                    print("El álbum no existe!!")

                otra = input("Desea actualizar otro stock (s/n)?: ").lower()
                if otra != "si":
                    break

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Debe seleccionar una opción válida!!")
    
def stock_genero(genero):
    total_stock = 0
    genero = genero.lower()
    for album_id in albums:
        album_genero = albums[album_id][2].lower()
        if album_genero == genero:
            total_stock += inventario[album_id][0]
    print(f"El stock total para {genero.capitalize()} es: {total_stock}")
    
def busqueda_anio(min, max):
    resultados = []
    for album_id in albums:
        anio = albums[album_id][3]
        stock = inventario[album_id][0]
        if min <= anio <= max and stock > 0:
            artista = albums[album_id][0]
            titulo = albums[album_id][1]
            resultados.append(f"{artista}--{titulo}")
    if resultados:
        resultados.sort()
        print("Los álbumes entre los años consultados son:", resultados)
    else:
        print("No hay álbumes en ese rango de años.")

def actualizar_stock(album_id, nueva_cantidad):
    if album_id in inventario:
        inventario[album_id][0] = nueva_cantidad
        return True
    else:
        return False