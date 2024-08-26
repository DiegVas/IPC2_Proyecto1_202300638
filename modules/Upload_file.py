import xml.etree.ElementTree as ET
import time
import sys


def Upload_file():
    print("\n---- Cargar archivo ----\n")
    RuteFile = input("Ingrese la ruta del archivo XML: ")
    Errors = []
    try:

        Show_progress_bar()

        tree = ET.parse(RuteFile)
        root = tree.getroot()

        if root.tag != "matrices":
            raise ValueError("El archivo XML debe tener una etiqueta raíz <matrices>")

        for matrix in root.findall("matriz"):
            name = matrix.get("nombre")
            n = int(matrix.get("n"))
            m = int(matrix.get("m"))

            if not name or n < 1 or m < 1:
                Errors.append("Atributos inválidos en la etiqueta <matriz>")

            print(f"Matriz: {name}, Filas: {n}, Columnas: {m}")

            for dato in matrix.findall("dato"):
                x = int(dato.get("x"))
                y = int(dato.get("y"))
                valor = dato.text

                if x < 1 or x > n or y < 1 or y > m:
                    Errors.append(f"Coordenadas inválidas en <dato>: x={x}, y={y}")

                print(f"Dato en ({x},{y}): {valor}")

    except ET.ParseError:
        Errors.append("Error al parsear el archivo XML")
    except FileNotFoundError:
        Errors.append("Archivo no encontrado")
    except Exception as e:
        Errors.append(f"Error: {e}")

    if Errors:
        print("\nErrores encontrados:")
        for error in Errors:
            print(error)


def Show_progress_bar():
    barra = [
        "[                    ]",
        "[=                   ]",
        "[==                  ]",
        "[===                 ]",
        "[====                ]",
        "[=====               ]",
        "[======              ]",
        "[=======             ]",
        "[========            ]",
        "[=========           ]",
        "[==========          ]",
        "[===========         ]",
        "[============        ]",
        "[=============       ]",
        "[==============      ]",
        "[===============     ]",
        "[================    ]",
        "[=================   ]",
        "[==================  ]",
        "[=================== ]",
        "[====================]",
    ]

    print("---- Cargando archivo ----")
    for estado in barra:
        sys.stdout.write("\r" + estado)
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n---- Archivo cargado. ----\n")
