import xml.etree.ElementTree as ET


def Extract_file(Circular_list):
    print("Escribiendo archivo de salida...")
    ruta = input("Ingrese la ruta donde se guardará el archivo XML: ")

    root = ET.Element("matrices")

    for matriz in Circular_list:
        matriz_element = ET.SubElement(
            root,
            "matriz",
            nombre=matriz.nombre,
            n=str(matriz.n),
            m=str(matriz.m),
            g=str(len(matriz.agrupar_filas())),
        )
        for (x, y), valor in matriz.datos.items():
            dato = ET.SubElement(matriz_element, "dato", x=str(x), y=str(y))
            dato.text = str(valor)
        filas_agrupadas = matriz.agrupar_filas()
        for idx, grupo in enumerate(filas_agrupadas):
            frecuencia = ET.SubElement(matriz_element, "frecuencia", g=str(idx + 1))
            frecuencia.text = str(len(grupo))

    tree = ET.ElementTree(root)
    tree.write(ruta, encoding="utf-8", xml_declaration=True)
    print(f"Archivo XML guardado en {ruta}")
