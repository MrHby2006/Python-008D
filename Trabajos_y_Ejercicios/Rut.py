
def validarRut(rut):
    mult = 2
    num = 0
    total = 0
    suma_total = 0
    resultado = 0
    resto = 0
    
    for caracter in reversed(rut):
        num = int(caracter)
        total = num * mult
        mult += 1
        if mult == 7:
            mult = 2
        suma_total = suma_total + total

    total1 =suma_total // 11
    total2 = suma_total % 11
    total3 = total1 * 11
    total4 = suma_total - total3

    dv = 11 - total4
    print(dv)
    if dv == 11:
        dv = 0
        print(f"{rut}-{str(dv)}")
    elif dv == 10:
        dv = "k"
        print(f"{rut}-{str(dv)}")
    else:
        print(f"{rut}-{str(dv)}")