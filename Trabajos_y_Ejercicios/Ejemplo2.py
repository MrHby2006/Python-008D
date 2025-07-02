
texto = "Letras y Texto"
for i in texto:
    if i.islower():
        print(i.upper(), end = " ")
    elif i.isupper():
        print(i.lower(), end = " ")
    else:
        print(i, end = " ")