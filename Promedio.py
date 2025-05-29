
print("Bienvenidos a el Promediador de Notas 3.0")

Nota_1 = float(input("Ingrese la primera nota: "))
Nota_2 = float(input("Ingrese la segunda nota: "))
Nota_3 = float(input("Ingrese la tercera nota: "))

Resultado = (Nota_1 + Nota_2 + Nota_3) / 3

print(Resultado)

if Resultado > 4.0:
    print("Felicidades, aprobaste")
elif Resultado < 4.0:
     print("Que pena, suerte para la proxima")