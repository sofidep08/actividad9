clientes = {}
opcion = 0
while opcion !=3:
    print("[1] Ingresar clientes")
    print("[2] Mostrar clientes registrados")
    print("[3] Salir")
    opcion=int(input("Elija una opcion: "))
    if opcion <=0 or opcion >3:
        print("Ingreso un dato incorrecto")
    else:
        match opcion:
            case 1:
                Cantidad= int(input("Ingrese la cantidad de clientes que desea registrar: "))
                for i in range(Cantidad):
                    print("Cliente #", i+1)
                    codigo_cliente=int(input("Ingrese el codigo de cliente: "))
                    clientes[codigo_cliente]={}
                    clientes[codigo_cliente]["nombre"] = input("Ingrese el nombre: ")
                    clientes[codigo_cliente]["visitas"] = {}

                    destinos=int(input("Ingrese la cantidad de destinos turísticos visitados (mínimo 1, máximo 5 ): "))
                    if destinos <= 0 or destinos >5:
                        print("Ingreso un dato incorrecto")
                    else:
                        for j in range(destinos):
                            codigo_viaje=int(input("Ingrese el codigo de viaje del destino: "))
                            destino= input("Destino ", j+1 , ": ")
                            clientes[codigo_cliente]["visitas"][codigo_viaje]={
                                "visita" : destino
                            }
                print("Cliente registrado")
            case 2:
                print("Clientese registrados")
