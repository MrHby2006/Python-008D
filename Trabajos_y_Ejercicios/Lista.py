
#Lista_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #//con datos númericos//

#for numero in Lista_numero:
#    print(f"El número actual es: {numero}")

#Lista_paises = ["Argentina", "Bolivia", "Chile", "Ecuador", "Colombia", "Brasil", "Paraguay", "Perú", "Uruguay", "Venezuela", "Guayana Francesa", "Surinam", "Guyana"] #//con datos textuales//

#for pais in Lista_paises:
#    print(f"El pais es: {pais}")

#lista_compuesta = ["brasil", 1, "argentina", 2] #//con datos mixtos//

#for elemento in lista_compuesta:
#    print(elemento)

#lista_paises = ["argentina", "brasil", "bolivia"] #//añadir un elemento a la lista//

#lista_paises.append("chile")

#for pais in lista_paises:
#    print(f"El pais es: {pais}")

#lista_paises = ["chile", "argentina", "colombia"] #//añadir un elemento en una poxición exacta//

#lista_paises.insert(1,"venezuela")

#for pais in lista_paises:
#    print(pais)

#milista = [1, 2, 3, "Juan", 4, 5] #//remover o quitar algo de la lista//

#milista.remove("Juan")

#for parte in milista:
#    print(parte)

#lista = [1, 2, 3, 4, 5, 6, 7] #//para cambiar el orden, ahora seria de derecha a izquierda//

#lista.reverse()

#for numero in lista:
#    print(numero)
    
milista = [3, 6, 1, 2, 7, 5, 4] #//para ordenar de menor a mayor

milista.sort()

for numero in milista:
    print(numero)