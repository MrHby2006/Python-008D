
def guardar(peliculas):
    cantidad = int(input("Ingrese la cantidad de peliculas a ingresar: "))
    for i in range(1,cantidad + 1):
            print(f"-----------------Guardar {i} Pelicula------------------")
            nombre = input("Ingrese el nombre de la pelicula: ").lower()
            genero = input("Ingrese el genero de la pelicula: ").lower()
            año = int(input("Ingrese el año de estreno: "))

            peliculas.append({
                "nombre": nombre,
                "genero": genero,
                "año": año
            })     
            
def mostrar(peliculas):
    for indice, pelicula in enumerate(peliculas):
            print(f"{indice + 1} - {pelicula["nombre"]} - {pelicula["genero"]} - {pelicula["año"]}")
            
def menu():
    print("--Tienda de peliculas--")
    print("1. Agregar peliculas")
    print("2. Mostrar peliculas")
    print("3. Eliminar pelicula")
    print("4. Buscar pelicula")
    print("5. Salir")
    
def buscar(peliculas):
    nombre = input("Ingrese la pelicula a buscar: ").lower()
    
    encontrado = None
    for pelicula in peliculas:
        if pelicula["nombre"] == nombre:
            encontrado = pelicula
            break
        
    if encontrado:
        print(f"Esta pelicula es del genero {encontrado["genero"]} y se estreno en el año {encontrado["año"]}")
    else:
        print("Pelicula no encontrada")
        
def eliminar(peliculas):
    nombre = input("Ingrese la pelicula que desea eliminar: ").lower()
    
    eliminado = False
    for i, pelicula in enumerate(peliculas):
        if pelicula["nombre"] == nombre:
            del peliculas[i]
            eliminado = True
            
    if eliminado:
        print("Pelicula eliminada exitosamente")
    else:
        print("No se pudo eliminar esta pelicula")