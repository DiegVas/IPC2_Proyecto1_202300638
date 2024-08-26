def Process_file(circular_list):
    print("Procesando archivo...")
    for matriz in circular_list:
        print(matriz.showData())
        print("Matriz de frecuencias:")
        print(matriz.matrix_patter_access().showData())
        print("Matriz reducida:")
        print(matriz.matrix_patter_access().sumar_filas_agrupadas(matriz).showData())
