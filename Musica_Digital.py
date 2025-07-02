albums = {
    "ALB001": ["a nigth at the opera", "queen", "rock", 1975, "vinilo"],
    
}



def menu():
    print("---Música Digital---")
    print("1. Stock por Genero")
    print("2. Búsqueda por Año de Lanzamiento")
    print("3. Actualizar Cantidad de Stock")
    print("4. Salir")
    
def main(opcion):
    menu()
    while True:
        try:
            opcion = int(input("Ingrese la opción a realizar: "))