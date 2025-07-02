
Texto = "        Harol Sarmiento Fernández"
Texto = Texto.strip(). lower()
Texto = Texto.upper()
Texto = Texto.replace("HAROL", "Handroll")
Texto_buscado = Texto.find("SARMIENTO")
Texto_dividido = Texto.split( )
print(Texto)
print(Texto_buscado)
print(Texto_dividido)

#Texto = "Llanos Juan"
#print(Texto[7:11]) #Solo escribira Juan (Subcadena)

#Nombre = "Antonia" #Se le asigna un valor, en este caso un nombre
#print(Nombre[0]) #Solo mostrara la primeta parte de el nombre (Cadena)

#nombre = input("Por favor ingrese su nombre: ") #Sera como el leer de Pseint
#apellidoP = input("Ingrese su apellido paterno: ") #Sera como el leer de Pseint
#apellidoM = input("Ingrese su apellido materno: ") #Sera como el leer de Pseint
#print(f"Su nombre es: {nombre} {apellidoP} {apellidoM}") #Concadenar
