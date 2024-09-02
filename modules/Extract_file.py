import xml.etree.ElementTree as ET
from classes.Matrix import CustomDict, CustomList, Node


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

        matriz_reducida = matriz.matrix_patter_access().sumar_filas_agrupadas(matriz)
        current = matriz_reducida.head
        while current:
            dato = ET.SubElement(
                matriz_element, "dato", x=str(current.x), y=str(current.y)
            )
            dato.text = str(current.valor)
            current = current.next

        filas_agrupadas = matriz.matrix_patter_access()
        patrones = CustomDict()
        g_counter = 1
        frecuencias = FrequencyDict()

        for i in range(1, filas_agrupadas.n + 1):
            patron = ""
            for j in range(1, filas_agrupadas.m + 1):
                patron += str(filas_agrupadas.obtener_dato(i, j))
            if patrones.get(patron) == 0:
                patrones.add(patron, g_counter)
                frecuencias.add(g_counter, 1)
                g_counter += 1
            else:
                g_value = patrones.get(patron)
                frecuencias.add(g_value, 1)

        for g_value in frecuencias.keys():
            frecuencia = ET.SubElement(matriz_element, "frecuencia", g=str(g_value))
            frecuencia.text = str(frecuencias.get(g_value))

    tree = ET.ElementTree(root)
    tree.write(ruta, encoding="utf-8", xml_declaration=True)
    print(f"Archivo XML guardado en {ruta}")


class FrequencyDict:
    def __init__(self):
        self.head = None

    def add(self, key, value):
        if not self.head:
            self.head = Node(key=key, value=value)
        else:
            current = self.head
            while current.next:
                if current.key == key:
                    current.value += value
                    return
                current = current.next
            if current.key == key:
                current.value += value
            else:
                current.next = Node(key=key, value=value)

    def get(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return 0

    def keys(self):
        current = self.head
        while current:
            yield current.key
            current = current.next
