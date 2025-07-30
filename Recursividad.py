while True:
    print("Bienvenido")
    print("1. Calcular el MCD")
    print("2. Cadena repetida")
    print("3. Cuantas veces aparece una letra")
    print("4. Decimal a Binario")
    print("5. Dígitos de un número")
    print("6. Salir")
    opcion=print("Seleccione la accion que desea realizar: ")
    match opcion:
        case "1":
            print("Calcular el MCD")
            def MCD(a, b):
                return 0
            a=int("Ingrese el primer número")
            b=int("Ingrese el segundo número")
            for a, b in (a*b/b):
                c=a*b/b
                print(f"El MCD: {a} y {b} es: {c}")
        case "2":
            print("Cadena repetida")
            def cadena(palabra,veces=0):
                if veces == len(palabra):
                    return 0
                if palabra[veces]== veces:
                    return contar(palabra,veces+1)+1
                else:
                    return contar(palabra,veces+1)
            if len(palabra)!=1:
                palabra=input("Ingrese una palabra: ")
                veces=input("Ingrese cuantas veces quiere que se repita: ")
            else:
                cantidad=contar(palabra*veces)
                print(f"{palabra}*{cantidad}.")
        case "3":
            print("Cuantas veces aparece una letra")
            def contar(frase,letra,aparece=0):
                if aparece == len(frase):
                    return 0
                if frase[aparece]== letra:
                    return contar(frase,letra,aparece+1)+1
                else:
                    return contar(frase,letra,aparece+1)
            frase=input("Ingrese una palabra: ")
            letra=input("Ingrese una letra para contar: ")
            if len(letra)!=1:
                print("Por favor ingresa una letra")
            else:
                cantidad=contar(frase,letra)
                print(f"la letra {letra} aparece {cantidad} veces.")
        case "4":
            print("Decimal a Binario")
        case "5":
            print("Digitos de un número")
        case "6":
            print("Saliendo.")
            break