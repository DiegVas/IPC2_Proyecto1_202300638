import time
import xml.etree.ElementTree as ET
from classes.Nodo import Node

# from classes.AgrupRow import NodeRow, CustomDict


class Matriz:
    def __init__(self, nombre, n, m):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.head = None

    def agregar_dato(self, x, y, valor):
        if x < 1 or x > self.n or y < 1 or y > self.m:
            raise ValueError("Coordenadas fuera de los límites de la matriz")
        new_node = Node(x=x, y=y, valor=valor)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def obtener_dato(self, x, y):
        current = self.head
        while current:
            if current.x == x and current.y == y:
                return current.valor
            current = current.next
        return None

    def showData(self):
        matriz_str = f"\n --- {self.nombre}, Filas: {self.n}, Columnas: {self.m} ----\n"

        for x in range(1, self.n + 1):
            for y in range(1, self.m + 1):
                matriz_str += f"{self.obtener_dato(x, y)} "
            matriz_str += "\n"
        return matriz_str

    def matrix_patter_access(self):

        mostrar_mensaje_con_puntos("Calculando matriz binaria")

        matrix_pattern = Matriz(f"{self.nombre}_pattern", self.n, self.m)
        for x in range(1, self.n + 1):
            for y in range(1, self.m + 1):
                valor = int(self.obtener_dato(x, y))
                if valor > 0:

                    matrix_pattern.agregar_dato(x, y, 1)
                else:
                    matrix_pattern.agregar_dato(x, y, 0)

        return matrix_pattern

    def agrupar_filas(self):
        filas_dict = CustomDict()

        for i in range(1, self.n + 1):
            fila = ""
            for j in range(1, self.m + 1):
                fila += str(self.obtener_dato(i, j)) + ","
            if filas_dict.get(fila):
                filas_dict.get(fila).append(i)
            else:
                filas_dict.add(fila, CustomList())
                filas_dict.get(fila).append(i)

        filas_agrupadas = CustomList()
        for filas in filas_dict.values():
            filas_agrupadas.append(filas)
        return filas_agrupadas

    def sumar_filas_agrupadas(self, otra_matriz):
        mostrar_mensaje_con_puntos("Agrupando filas")

        filas_agrupadas = self.agrupar_filas()

        mostrar_mensaje_con_puntos("Sumando filas")

        resultado = Matriz("Matriz Reducida", len(filas_agrupadas), self.m)

        for idx, grupo in enumerate(filas_agrupadas):
            for j in range(1, self.m + 1):
                suma = sum(int(otra_matriz.obtener_dato(i, j)) for i in grupo)
                resultado.agregar_dato(idx + 1, j, suma)

        return resultado

    def exportar_a_xml(self, ruta):
        root = ET.Element(
            "matriz",
            nombre=self.nombre,
            n=str(self.n),
            m=str(self.m),
            g=str(len(self.agrupar_filas())),
        )
        current = self.head
        while current:
            dato = ET.SubElement(root, "dato", x=str(current.x), y=str(current.y))
            dato.text = str(current.valor)
            current = current.next

        filas_agrupadas = self.agrupar_filas()
        for idx, grupo in enumerate(filas_agrupadas):
            frecuencia = ET.SubElement(root, "frecuencia", g=str(idx + 1))
            frecuencia.text = str(len(grupo))

        tree = ET.ElementTree(root)
        tree.write(ruta, encoding="utf-8", xml_declaration=True)


def mostrar_mensaje_con_puntos(mensaje):
    print(mensaje, end="", flush=True)
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print()


class Node:
    def __init__(self, x=None, y=None, valor=None, key=None, value=None):
        self.x = x
        self.y = y
        self.valor = valor
        self.key = key
        self.value = value
        self.next = None


class CustomDict:
    def __init__(self):
        self.head = None

    def add(self, key, value):
        if not self.head:
            self.head = Node(key=key, value=value)
        else:
            current = self.head
            while current.next:
                if current.key == key:
                    current.value.append(value)
                    return
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = Node(key=key, value=value)

    def get(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return 0

    def values(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


class CustomList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value=value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
