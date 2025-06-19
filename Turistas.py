opcion = 0

turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
    }

def turistas_por_pais(pais):
    resultado = [datos[0] for datos in turistas.values() if datos[1].lower() == pais.lower()]
    if resultado:
        print(resultado)
    else:
        print("No hay turistas de ese pais.")
        
def turistas_por_mes(mes):
    total = len(turistas)
    coincidencias = 0
    for datos in turistas.values():
        fecha = datos[2]
        mes_turista = int(fecha.split("-")[1])
        if mes_turista == mes:
            coincidencias += 1
    porcentaje = (coincidencias / total) * 100
    return round(porcentaje, 1)

def eliminar_turista():
    nombre = input("Ingrese el nombre del turista a eliminar: ").strip().lower()
    clave_a_eliminar = None
    for clave, datos in turistas.items():
        if datos[0].strip().lower() == nombre:
            clave_a_eliminar = clave
            break
    if clave_a_eliminar:
        del turistas[clave_a_eliminar]
        print("Turista eliminado con éxito.")
    else:
        print("Turista no encontrado. No se pudo eliminar.")



def menu():
    while True:
        print("\nMENU PRINCIPAL")
        print("1.- Turistas por pais.")
        print("2.- Turista por mes.")
        print("3.- Eliminar turista.")
        print("4.- Salir.")
        opcion = input("Ingrese opción: ").strip()

        if opcion == "1":
            pais = input("Ingrese pais a buscar: ")
            turistas_por_pais(pais)

        elif opcion == "2":
            while True:
                try:
                    mes = int(input("Ingrese mes a buscar: "))
                    if 1 <= mes <= 12:
                        porcentaje = turistas_por_mes(mes)
                        print(f"El número de turistas equivale al {porcentaje} % del total.")
                        break
                    else:
                        print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
                except ValueError:
                    print("Debe ingresar un número entero válido.")

        elif opcion == "3":
            eliminar_turista()

        elif opcion == "4":
            print("Programa terminado...")
            break

        else:
            print("Debe seleccionar una opción válida.")