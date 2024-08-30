import xml.etree.ElementTree as ET


def Extract_file(Circular_list):
    print("Escribiendo archivo de salida...")
    ruta = input("Ingrese la ruta donde se guardará el archivo XML: ")

    root = ET.Element("matrices")

    for matriz in Circular_list:

        print(matriz.matrix_patter_access().showData())
        print(matriz.showData())

        matriz_element = ET.SubElement(
            root,
            "matriz",
            nombre=matriz.nombre,
            n=str(matriz.n),
            m=str(matriz.m),
            g=str(len(matriz.matrix_patter_access().agrupar_filas())),
        )
        for (x, y), valor in (
            matriz.matrix_patter_access().sumar_filas_agrupadas(matriz).datos.items()
        ):
            dato = ET.SubElement(matriz_element, "dato", x=str(x), y=str(y))
            dato.text = str(valor)

        filas_agrupadas = matriz.matrix_patter_access()
        patrones = {}
        g_counter = 1
        for i in range(1, filas_agrupadas.n + 1):
            patron = tuple(
                filas_agrupadas.obtener_dato(i, j)
                for j in range(1, filas_agrupadas.m + 1)
            )
            if patron not in patrones:
                patrones[patron] = g_counter
                g_counter += 1

        frecuencias = {g: 0 for g in patrones.values()}
        for i in range(1, filas_agrupadas.n + 1):
            patron = tuple(
                filas_agrupadas.obtener_dato(i, j)
                for j in range(1, filas_agrupadas.m + 1)
            )
            g_value = patrones[patron]
            frecuencias[g_value] += 1

        for g_value, count in frecuencias.items():
            frecuencia = ET.SubElement(matriz_element, "frecuencia", g=str(g_value))
            frecuencia.text = str(count)

    tree = ET.ElementTree(root)
    tree.write(ruta, encoding="utf-8", xml_declaration=True)
    print(f"Archivo XML guardado en {ruta}")
