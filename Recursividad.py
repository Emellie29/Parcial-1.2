while True:
    print("Bienvenido")
    print("1. Calcular el MCD")
    print("2. Cadena repetida")
    print("3. Cuantas veces aparece una letra")
    print("4. Decimal a Binario")
    print("5. Dígitos de un número")
    print("6. Salir")
    opcion=print("Seleccione una opcion: ")
    match opcion:
        case "1":
            print("Calcular el MCD")
            def MCD(a, b):
                return 0
            a=int("Ingrese el primer número")
            b=int("Ingrese el segundo número")
            MCD(a, b)
        case "2":
            print("Cadena repetida")
        case "3":
            print("Cuantas veces aparece una letra")
            def contarpalabra(letra,palabra):
                return 0
            letra=input("Ingresa una letra: ")
            palabra=input("Ingresa una palabra: ")
            contarpalabra(letra,palabra)
        case "4":
            print("Decimal a Binario")
        case "5":
            print("Digitos de un número")
        case "6":
            print("Saliendo.")
            break
        case _:
            print("Opcion no valida")