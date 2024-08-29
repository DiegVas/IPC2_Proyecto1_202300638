def Process_file(circular_list):
    nombre_matriz = input("Ingrese el nombre de la matriz a procesar: ")
    matriz_encontrada = None

    for matriz in circular_list:
        if matriz.nombre == nombre_matriz:
            matriz_encontrada = matriz
            break

    if matriz_encontrada:
        print(f"\n Procesando la matriz: {matriz_encontrada.nombre} \n ")

        print("---- Matriz reducida ----\n")
        print(
            matriz_encontrada.matrix_patter_access()
            .sumar_filas_agrupadas(matriz_encontrada)
            .showData()
        )
    else:
        print(f"Error: No se encontró una matriz con el nombre '{nombre_matriz}'")
