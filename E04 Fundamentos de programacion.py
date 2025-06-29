def menu_principal():
    while True:
        print("\n****TOTEM AUTOATENCIÓN RESERVA STRIKE****")
        print("1.- Reservar zapatillas")
        print("2.- Buscar zapatillas reservadas.")
        print("3.- Ver stock de reservas.")
        print("4.- Salir.")
        
        try:
            opcion =int(input("Ingrese la opción que desea: "))
            
            match opcion:
                case 1:
                    reservar_zapatillas()
                case 2:
                    buscar_zapatillas_reservadas()
                case 3:
                    ver_stock_reservas()
                case 4:
                    salir()
                    break
                case _:
                    print("Debe ingresar una opción válida!!")
        except:
            print("Favor ingrese una opción entre 1 y 4.")    

def validaciones():
    #Este bloque valida que el usuario ingresado no este repetido.
    while True:
        
        nombre_valido = True
        nombre = input("Ingrese su nombre: ")
        for usuario in usuarios_con_reserva:
            if usuario["nombre"] == nombre:
                print("Este usuario ya cuenta con una reserva.")
                nombre_valido = False
                break
        if nombre_valido:
            break
    
    #Este bloque valida la frase secreta
    frase_secreta = input("Ingrese la frase secreta: ")    
    validacion_frase_secreta = False
    if frase_secreta == "EstoyEnListaDeReserva":
        print("Reserva existosa!")
        validacion_frase_secreta = True
    else:
        print("Error: palabra clave incorrecta. Reserva no realizada.")

    #salida del bucle
    if nombre_valido and validacion_frase_secreta:
        return nombre
    
def reservar_zapatillas():
    if stock_reserva[0] > 0:
        print("\n****Sistema de reserva****")
        nombre = validaciones()
        usuario = {
            "nombre": nombre,
            "cantidad_de_reservas": 1,
            "categoria":"Estándar"
        }       
        usuarios_con_reserva.append(usuario)
        stock_reserva[0] -= 1
        stock_reserva[1] += 1
    else:
        print("No hay stock disponible para reserva.")
    
def buscar_zapatillas_reservadas():
    print("****Sistema de busqueda de reservas****")
    nombre_buscado = input("Nombre del comprador a buscar: ")
    
    nombre_encontrado=False
    for usuario in usuarios_con_reserva:
        if usuario["nombre"] == nombre_buscado:
            nombre_encontrado = True
            print(f"Reserva encontrada: {nombre_buscado} - {usuario['cantidad_de_reservas']} par(es) ({usuario['categoria']})")
            if stock_reserva[0] > 0:
                while True:
                    opcion = input("\n¿Desea pagar adicional para VIP y reservar 2 pares? (si/no): ")
                    
                    match opcion:
                        case "si":
                            usuario["cantidad_de_reservas"] = 2
                            usuario["categoria"] = "VIP"
                            stock_reserva[0] -= 1
                            stock_reserva[1] += 1
                            break
                        case "no":
                            print("Manteniendo reserva actual.")
                            break
                        case _:
                            print("Opcion inválida. Por favor, intente nuevamente.")
            else:
                print("No hay stock para upgrade a VIP.")
    if not nombre_encontrado:
        print(f"El usuario {nombre_buscado} no tiene reservas.")

def ver_stock_reservas():
    print(f"Pares reservados: {stock_reserva[1]}")
    print(f"Pares disponibles: {stock_reserva[0]}")

def salir():
    print("Programa terminado...")

#main()
usuarios_con_reserva = []
stock_reserva = [20,0]
menu_principal()
