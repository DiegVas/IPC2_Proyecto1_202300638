import xml.etree.ElementTree as ET
import time
import sys

from classes.Matrix import Matriz


def Upload_file():
    print("\n---- Cargar archivo ----\n")

    ruteFile = input("Ingrese la ruta del archivo XML: ")

    Show_progress_bar()
    print("\n---- Ruta del archivo XML guardada con exito ----\n")

    Errors = []
    try:

        tree = ET.parse(ruteFile)
        root = tree.getroot()

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
        return ""

    return ruteFile


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
        "[====================]\n",
    ]

    print("---- Guardando archivo ----")
    for estado in barra:
        sys.stdout.write("\r" + estado)
        sys.stdout.flush()
        time.sleep(0.1)
