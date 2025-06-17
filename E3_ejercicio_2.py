numero_case_1=None
numero_mayor=0
suma=0
contador=0

while True:
    try:
        opc_menu_principal=int(input("***MENU PRINCIPAL***\n1.- Ingresar número\n2.- Mostrar mayor\n3.- Mostar menor\n4.- Salir\nDigite su opción: "))
        match opc_menu_principal:
            case 1:
                while True:
                    try:
                        numero_case_1=int(input("\nIngrese un número entero entre 1 y 100: "))
                        
                        if 1<=numero_case_1<=100:
                            print("Ingreso exitoso\n")
                            suma += numero_case_1
                            contador += 1
                            if numero_case_1>=numero_mayor:
                                numero_mayor=numero_case_1
                            break
                        else:
                            print("Número inválido. Debe ingresar un número entre 0 y 100.")
                      
                    except ValueError:
                        print("Ingreso inválido. Por favor digite un número entero.")
            case 2:
                if numero_case_1 != None:
                    print(f"El mayor número ingresado fue: {numero_mayor} \n")
                else: 
                    print("No se han ingresado números\n")
            case 3:
                if numero_case_1 != None:
                    print(suma/contador,"\n")
                else:
                    print("No se han ingresado números.\n")
            case 4:
                print("\nFin del programa. Adiós.")
                break
            case _:
                print("Opción fuera de rango. Por favor digitar una opción entre 1 y 4.")
    except ValueError:
        print("Caracter inválido. Por favor digitar una opción entre 1 y 4.")