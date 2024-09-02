import xml.etree.ElementTree as ET
from classes.ErrorManager import ErrorManager


def Upload_file():
    print("\n---- Cargar archivo ----\n")

    ruteFile = input("Ingrese la ruta del archivo XML: ")

    print("\n---- Ruta del archivo XML guardada con exito ----\n")

    error_manager = ErrorManager()
    try:
        tree = ET.parse(ruteFile)
        root = tree.getroot()

    except ET.ParseError:
        error_manager.add_error("Error al parsear el archivo XML")
    except FileNotFoundError:
        error_manager.add_error("Archivo no encontrado")
    except Exception as e:
        error_manager.add_error(f"Error: {e}")

    if error_manager.has_errors():
        print("\nErrores encontrados:")
        print(error_manager.get_errors())
        return ""

    return ruteFile
