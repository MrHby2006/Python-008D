
productos = ["huevos","leche","papas fritas", "yogurth"]

for producto in productos:
    print(productos)
    print("------------")
    eliminar = input("Escribe lo que deseas eliminar: ")
    productos.remove(eliminar)
    print(productos)