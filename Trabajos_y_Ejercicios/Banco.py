#Saldo inicial de la cuenta
saldo = 100000
cuenta_ahorro = 0

#Loop principal del programa
while True:
    #Mostrar menu
    print("Bienvenido al Banco del País, seleccione una opción")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Agregar saldo")
    print("4. Hacer un deposito a cuenta de ahorro")
    print("5. Traspasar sus ahorros a su saldo")
    print("6. Salir")
    
    #Solicutar opción al usuario
    opcion = input("Selecciona una opción (1-6): ")
    
    #Realizar acciones según la opción seleccionada
    if opcion == "1":
        print(f"Tu saldo actual es : ${saldo}")
    elif opcion == "2":
        cantidad_retiro = float(input("Ingrese la cantidad a retirar: $"))
        if cantidad_retiro <= saldo:
            saldo -= cantidad_retiro
            print(f"Has retirado ${cantidad_retiro}. Saldo actual: ${saldo}")
        else:
            print("Saldo insuficiente. No es posible realizar el retiro")
    elif opcion == "3":
        cantidad_añadida = float(input("Ingrese la cantidad a añadir: $"))
        saldo += cantidad_añadida
        print(f"Has añadido ${cantidad_añadida}. Saldo actual: ${saldo}")
    elif opcion == "4":
        cantidad_ahorrada = float(input("Ingrese la cantidad que desea añadir a su ahorro: $"))
        if cantidad_ahorrada <= saldo:
            saldo -= cantidad_ahorrada
            cuenta_ahorro += cantidad_ahorrada
            print(f"Has añadido ${cantidad_ahorrada} a tu cuenta de ahorro. Saldo actual: ${saldo}. Saldo actual de ahorro: ${cuenta_ahorro}")
        else:
            print("Saldo insuficiente. No es posible realizar el traspaso")
    elif opcion == "5":
        saldo += cuenta_ahorro
        cuenta_ahorro -= cuenta_ahorro
        print(f"Has traspasado tus ahorros a tu cuenta. Saldo actual: ${saldo}. Saldo actual de ahorro: ${cuenta_ahorro}")
    elif opcion == "6":
        print("Gracias por utilizar el Cajero")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida")