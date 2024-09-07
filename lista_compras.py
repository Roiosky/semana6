lista_compras = []

while True:
    # Menu principal de opciones
    print("\nMenú:")
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Mostrar lista")
    print("4. Salir")

    opcion = input("Selecciona una opción (1/2/3/4): ")
    
    # Manejar las opciones del menú
    if opcion == '1':
        # Opción 1: Agregar artículo
        articulo = input("Ingrese el nombre del artículo a agregar: ")
        lista_compras.append(articulo)
        print(f"'{articulo}' ha sido agregado a la lista.")
    
    elif opcion == '2':
        # Opción 2: Eliminar artículo
        if len(lista_compras) == 0:
            print("La lista de compras está vacía.")
        else:
            print("Lista de compras actual:")
            for idx in range(len(lista_compras)):
                print(f"{idx}. {lista_compras[idx]}")
            indice = int(input("Ingrese el índice del artículo a eliminar: "))
            # Aquí puede ocurrir un error si el índice está fuera de rango
            if indice >= 0 and indice < len(lista_compras):
                lista_compras.pop(indice)
                print("Artículo eliminado.")
            else:
                print("Índice fuera de rango.")
    
    elif opcion == '3':
        # Opción 3: Mostrar lista
        if len(lista_compras) == 0:
            print("La lista de compras está vacía.")
        else:
            print("Lista de compras:")
            for item in lista_compras:
                print("- " + item)
    
    elif opcion == '4':
        # Opción 4: Salir
        print("¡Gracias por usar el programa de lista de compras! Hasta luego.")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")
