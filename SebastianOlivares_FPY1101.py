#Funciones
def menu():
    continuar=True
    while continuar:
        print("\n****Menú de inicio****")
        print("1.- Comprar departamento")
        print("2.- Mostrar departamento")
        print("3.- Listado de compradores")
        print("4.- Ganancias totales")
        print("5.- Salir")
        opcion_menu=input("Ingrese su opcion: ")
        
        match opcion_menu:
            case "1":
                comprar_departamento()
            case "2":
                mostrar_departamentos()
            case "3":
                lista_compradores()
            case "4":
                ganancias_totales()
            case "5":
                print("\nSaliendo del sistema. Hasta pronto.")
                #Aquí debería mostrar nombre, apellido y fecha solicitado según enunciado, sin embargo, no especifica de quién (vendedor o comprador) ni en qué momento pedirlo.
                continuar=False
            case _:
                print("\nOpción inválida. Por favor, vuelva a intentar.")
        input("\npresione enter para continuar")
        
def comprar_departamento():
    print("\n***Comprar departamento***")
    mostrar_departamentos()
    continuar = True
    while(continuar):
        departamento_por_comprar=input("\nIngrese el departamento que desea comprar: ").upper()
        
        for idx in edificio:
            if idx["depto"] == departamento_por_comprar:
                if idx["disponible"]:
                    comprador=input("Ingrese su rut: ") # en virtud del tiempo dejaré el rut como str y no int para ahorrar el manejo de errores (try except)
                    print("Compra realizada con éxito.")
                    match idx["tipo"]:
                        case "A":
                            tipo_a[1] += 1
                        case "B":
                            tipo_b[1] += 1
                        case "C":
                            tipo_c[1] += 1
                        case "D":
                            tipo_d[1] += 1
                    compradores.append(comprador)
                    idx["disponible"]=False
                    continuar = False
                else:
                    print("Departamento no disponible. Elija otro.")
        
        if continuar:              
            print("Departamento inválido. Por favor, ingrese nuevamente.")
            
def mostrar_departamentos():
    print("\n***Mostrar departamento***\n")
    for i in range(len(edificio)):
        if "D" in edificio[i]["depto"]:
            if edificio[i]["disponible"]:
                print(edificio[i]["depto"])
            else:
                print(" X ")
        else:
            if edificio[i]["disponible"]:
                print(edificio[i]["depto"], end=" | ")
            else:
                print(" X ", end=" | ")
             

def lista_compradores():
    compradores.sort()
    print(compradores)

    
def ganancias_totales():
    cantidad_compras_por_tipo=[tipo_a , tipo_b , tipo_c , tipo_d]
    ganancia=0
    
    print("\n***Ganancias totales***\n")

    tipos = ["A", "B", "C", "D"]
    print("Tipo de departamento | cantidad | Total")        
    for i, tipo in zip(cantidad_compras_por_tipo, tipos):
        columnas_1_2 = "    |    ".join([i[0], str(i[1])])
        total_tipo = i[1] * valor[tipo]
        print(f"{columnas_1_2}     | {total_tipo} UF")

    for idx in edificio:
        if not idx["disponible"]:
            ganancia += idx["valor"]
    total_compras = sum(i[1] for i in cantidad_compras_por_tipo)
    
    print (f"Total               ",f"|    {total_compras}     | {ganancia}")
                    

#Edificio
edificio=[]
valor={
    "A":3800,
    "B":3000,
    "C":2800,
    "D":3500
}
for piso in range(1,11):
    for tipo in "DCBA":
        if piso < 10:
            depto= tipo + "0" + str(piso)
        else:
            depto= tipo + str(piso)
            
        valor_por_tipo=valor[tipo]
               
        departamento={
            "depto": depto,
            "disponible": True,
            "comprador":None,
            "tipo":tipo,
            "valor":valor_por_tipo
        }
        edificio.insert(0,departamento)

#constantes y variables globales
compradores=[]
tipo_a = ["Tipo A 3.800 UF: ", 0]
tipo_b = ["Tipo B 3.000 UF: ", 0]
tipo_c = ["Tipo A 2.800 UF: ", 0]
tipo_d = ["Tipo A 2.800 UF: ", 0]

#main()
menu()