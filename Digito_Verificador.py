RUN = ""

mult = 2
num = 0
total = 0
suma_total = 0
resultado = 0
resto = 0

print("----Dígito verificador del RUN----")
RUN = input("Ingrese su run sin puntos y sin el digito verificador: ")

for caracter in reversed(RUN):
    num = int(caracter)
    total = num * mult
    mult += 1
    if mult == 7:
        mult = 2
    suma_total = suma_total + total
    
total1 = suma_total // 11
total2 = suma_total % 11
total3 = total1 * 11
total4 = suma_total - total3

dv = 11 - total4
print(dv)
if dv == 11:
    dv = 0
    print(f"{RUN}-{str(dv)}")
elif dv == 10:
    dv = "k"
    print(f"{RUN}-{str(dv)}")
else:
    print(f"{RUN}-{str(dv)}")