
#Definimos las vocales
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

ContadorVocales = 0
ContadorConsonantes = 0

texto = input("Ingrese un texto: ")

for caracter in texto:
    #Verificamos si el caracter es una Letra
    if caracter.isalpha():
        #Verifica si es una vocal
        if caracter in vocales:
            ContadorVocales = ContadorVocales + 1
        else:
            ContadorConsonantes = ContadorConsonantes + 1

print(f"Cantidad de vocales: {ContadorVocales}")
print(f"Cantidad de consonantes: {ContadorConsonantes}")