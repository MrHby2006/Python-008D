
colores = ["rojo", "verde", "azul", "naranja"]

for color in colores:
    print(f"El color actual es: {color}")
    
print("---------------------------------")

colores.append("negro")
colores.insert(1, "amarillo")
colores.remove("rojo")

for color in colores:
    print(f"El color actual es: {color}")