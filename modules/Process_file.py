import xml.etree.ElementTree as ET
from classes.Matrix import Matriz
from classes.ErrorManager import ErrorManager


def Process_file(circular_list, ruteFile):

    error_manager = ErrorManager()
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
                error_manager.add_error("Atributos inválidos en la etiqueta <matriz>")

            if circular_list.exists(name):
                error_manager.add_error(f"La matriz {name} ya existe en la lista")
            else:
                MatrizData = Matriz(name, n, m)

                print(f"Matriz: {name}, Filas: {n}, Columnas: {m}")

                for dato in matrix.findall("dato"):
                    x = int(dato.get("x"))
                    y = int(dato.get("y"))
                    valor = dato.text

                    if x < 1 or x > n or y < 1 or y > m:
                        error_manager.add_error(
                            f"Coordenadas inválidas en <dato>: x={x}, y={y}"
                        )
                    else:
                        MatrizData.agregar_dato(x, y, valor)

            circular_list.agregar(MatrizData)

    except Exception as e:
        error_manager.add_error(f"Error: {e}")

    if error_manager.has_errors():
        print("\nErrores encontrados:")
        print(error_manager.get_errors())
        print("")

    for matriz in circular_list:

        print(f"\n Procesando la matriz: {matriz.nombre} \n")

        print("---- Matriz original ----\n")
        print(matriz.showData())
        print("---- Matriz reducida ----\n")
        print(matriz.matrix_patter_access().sumar_filas_agrupadas(matriz).showData())
