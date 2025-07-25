def sumar(cantidades):
    if cantidades==0:
        return cantidades
    else:
        return cantidades + sumar(cantidades+1)

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
                            lugar= input("ingrese el lugar: ")
                            clientes[codigo_cliente]["visitas"][codigo_viaje]={
                                "visita" : lugar
                            }
                print("Cliente registrado")
            case 2:
                print("Clientese registrados")
                for codigo_cliente, datos in clientes.items():
                    print(f"Codigo de cliente: {codigo_cliente}")
                    print(f"Nombre: {datos['nombre']}")

                    for codigo_viaje, lugares in datos["visitas"].items():
                        print(f"Codigo de viaje: {codigo_viaje}")
                        print("Destino: ", lugares["destino"])

                print("Total de desinos visitados por todos los clientes ", sumar(()))
            case 3:
                print("Saliendo del menu...")