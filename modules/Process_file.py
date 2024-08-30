import xml.etree.ElementTree as ET
from classes.Matrix import Matriz


def Process_file(circular_list, ruteFile):

    Errors = []
    try:

        # Show_progress_bar()
        tree = ET.parse(ruteFile)
        root = tree.getroot()

        if root.tag != "matrices":
            raise ValueError("El archivo XML debe tener una etiqueta raíz <matrices>")

        for matrix in root.findall("matriz"):
            name = matrix.get("nombre")
            n = int(matrix.get("n"))
            m = int(matrix.get("m"))

            if not name or n < 1 or m < 1:
                Errors.append("Atributos inválidos en la etiqueta <matriz>")

            if circular_list.exists(name):
                Errors.append(f"La matriz {name} ya existe en la lista")
            else:
                MatrizData = Matriz(name, n, m)

                print(f"Matriz: {name}, Filas: {n}, Columnas: {m}")

                for dato in matrix.findall("dato"):
                    x = int(dato.get("x"))
                    y = int(dato.get("y"))
                    valor = dato.text

                    if x < 1 or x > n or y < 1 or y > m:
                        Errors.append(f"Coordenadas inválidas en <dato>: x={x}, y={y}")
                    else:
                        MatrizData.agregar_dato(x, y, valor)

            circular_list.agregar(MatrizData)

    except Exception as e:
        Errors.append(f"Error: {e}")

    if Errors:
        print("\nErrores encontrados:")
        for error in Errors:
            print(error)
        print("")

    for matriz in circular_list:

        print(f"\n Procesando la matriz: {matriz.nombre} \n")

        print("---- Matriz original ----\n")
        print(matriz.showData())
        print("---- Matriz reducida ----\n")
        print(matriz.matrix_patter_access().sumar_filas_agrupadas(matriz).showData())
