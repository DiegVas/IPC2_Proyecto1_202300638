import graphviz


def Generate_graph(circular_list):
    nombre_matriz = input("Ingrese el nombre de la matriz a procesar: ")
    matriz_encontrada = None

    for matriz in circular_list:
        if matriz.nombre == nombre_matriz:
            matriz_encontrada = matriz
            break

    if matriz_encontrada:
        # Obtener dimensiones de la matriz
        filas = matriz_encontrada.n
        columnas = matriz_encontrada.m

        # Crear el gráfico con Graphviz
        dot = graphviz.Digraph(comment=nombre_matriz)

        dot.node("name", label=nombre_matriz, shape="component")
        dot.node("Info", label=f"Filas: {filas}\nColumnas: {columnas}", shape="tab")

        dot.edge("name", "Info")

        # Añadir nodos para los valores de la matriz
        for i in range(1, filas + 1):
            for j in range(1, columnas + 1):
                valor = matriz_encontrada.obtener_dato(i, j)
                dot.node(f"{i}{j}", label=str(valor), shape="Msquare")

                if i == 1:
                    dot.edge("Info", f"{i}{j}")
                else:
                    dot.edge(f"{i - 1}{j}", f"{i}{j}")

        # Guardar el gráfico en un archivo PDF
        dot.render(f"{nombre_matriz}_grafica", format="pdf")

        # Matriz reducida
        matriz_reducida = (
            matriz_encontrada.matrix_patter_access().sumar_filas_agrupadas(
                matriz_encontrada
            )
        )

        filas = matriz_reducida.n
        columnas = matriz_reducida.m

        # Crear el gráfico con Graphviz
        dot = graphviz.Digraph(comment=nombre_matriz)

        dot.node("name", label=f"{nombre_matriz} reducida", shape="component")
        dot.node("Info", label=f"Filas: {filas}\nColumnas: {columnas}", shape="tab")

        dot.edge("name", "Info")

        # Añadir nodos para los valores de la matriz
        for i in range(1, filas + 1):
            for j in range(1, columnas + 1):
                valor = matriz_reducida.obtener_dato(i, j)
                dot.node(f"{i}{j}", label=str(valor), shape="Msquare")

                if i == 1:
                    dot.edge("Info", f"{i}{j}")
                else:
                    dot.edge(f"{i - 1}{j}", f"{i}{j}")

        # Guardar el gráfico en un archivo PDF
        dot.render(f"{nombre_matriz}_grafica_reducida", format="pdf")

    else:
        print(f"Error: No se encontró una matriz con el nombre '{nombre_matriz}'")
