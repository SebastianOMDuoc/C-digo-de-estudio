contador_esquema_completo=0
contador_esquema_incompleto=0

while True:
    try:
        registro_personas=int(input("Ingrese la cantidad de personas a registrar: "))
        break
    except:
        print("Error en el ingreso de registro. Por favor intente con un número entero")
    
for i in range(registro_personas):
    while True:
        try:
            condicion_esquema=int(input("Ingrese cantidad de dosis recibidas: "))
            if condicion_esquema < 3:
                print("Esquema incompleto")
                contador_esquema_incompleto += 1
                break
            elif condicion_esquema == 3:
                print("Esquema completo")
                contador_esquema_completo += 1
                break
            else:
                print("Valor ingresado mayor a 1. Por favor, vuelva a ingresar el número de dosis correcto.")
                    
        except:
            print("Error en el ingreso de dosis recibidas. Por favor intente con un número entero")

print(f"\n- Se registraron {contador_esquema_completo} con esquema completo\n- Se registraron {contador_esquema_incompleto} con esquema incompleto")