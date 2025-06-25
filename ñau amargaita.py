clientes = {}

while True:
    print("SISTEMA DE GESTIÓN DE CLIENTES")
    print("1.- Registrar nuevo cliente")
    print("2.- Buscar cliente por ID")
    print("3.- Mostrar todos los clientes")
    print("4.- Eliminar cliente")
    print("5.- Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id_cliente = input("Ingrese el ID del cliente: ")
        if id_cliente in clientes:
            print("El cliente con este ID ya existe.\n")
        else:
            nombre = input("Ingrese el nombre del cliente: ")
            correo = input("Ingrese el correo del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            clientes[id_cliente] = {
                "nombre": nombre,
                "correo": correo,
                "telefono": telefono
            }
            print("Cliente registrado correctamente.\n")

    elif opcion == "2":
        id_cliente = input("Ingrese el ID del cliente a buscar: ")
        if id_cliente in clientes:
            cliente = clientes[id_cliente]
            print(f"\nID: {id_cliente}")
            print(f"Nombre: {cliente['nombre']}")
            print(f"Correo: {cliente['correo']}")
            print(f"Teléfono: {cliente['telefono']}\n")
        else:
            print("Cliente no encontrado.\n")

    elif opcion == "3":
        if not clientes:
            print("No hay clientes registrados.\n")
        else:
            print("\nLista de Clientes:")
            for id_cliente, datos in clientes.items():
                print(f"\nID: {id_cliente}")
                print(f"Nombre: {datos['nombre']}")
                print(f"Correo: {datos['correo']}")
                print(f"Teléfono: {datos['telefono']}")
            print()

    elif opcion == "4":
        id_cliente = input("Ingrese el ID del cliente a eliminar: ")
        if id_cliente in clientes:
            del clientes[id_cliente]
            print("Cliente eliminado correctamente.\n")
        else:
            print("Cliente no encontrado.\n")

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Intente nuevamente.\n")
 
