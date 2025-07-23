opcion = 0
while opcion !=3:
    print("[1] Ingresar clientes")
    print("[2] Mostrar clientes registrados")
    print("[3] Salir")
    opcion=int(input("Elija una opcion: "))
    if opcion <=0 or opcion >3:
        print("Ingreso un dato incorrecto")
