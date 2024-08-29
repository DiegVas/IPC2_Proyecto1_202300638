import time
import xml.etree.ElementTree as ET


class Matriz:
    def __init__(self, nombre, n, m):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.datos = {}

    def agregar_dato(self, x, y, valor):
        if x < 1 or x > self.n or y < 1 or y > self.m:
            raise ValueError("Coordenadas fuera de los límites de la matriz")
        self.datos[(x, y)] = valor

    def obtener_dato(self, x, y):
        return self.datos.get((x, y), None)

    def showData(self):
        matriz_str = f"Matriz: {self.nombre}, Filas: {self.n}, Columnas: {self.m}\n"
        print("\n---- Matriz ----\n")
        for x in range(1, self.n + 1):
            for y in range(1, self.m + 1):
                matriz_str += f"{self.obtener_dato(x, y)} "
            matriz_str += "\n"
        return matriz_str

    def obtain(self, x, y):
        return self.datos.get((x, y), None)

    def matrix_patter_access(self):

        mostrar_mensaje_con_puntos("Calculando matriz binaria")

        matrix_pattern = Matriz(f"{self.nombre}_pattern", self.n, self.m)
        for x in range(1, self.n + 1):
            for y in range(1, self.m + 1):
                valor = int(self.obtener_dato(x, y))
                if valor > 0:

                    matrix_pattern.datos[(x, y)] = 1
                else:
                    matrix_pattern.datos[(x, y)] = 0

        print("\nMatriz binaria calculada.")

        return matrix_pattern

    def agrupar_filas(self):
        filas_dict = {}

        for i in range(1, self.n + 1):
            fila = tuple(self.obtener_dato(i, j) for j in range(1, self.m + 1))
            if fila in filas_dict:
                filas_dict[fila].append(i)
            else:
                filas_dict[fila] = [i]

        filas_agrupadas = list(filas_dict.values())
        return filas_agrupadas

    def sumar_filas_agrupadas(self, otra_matriz):

        mostrar_mensaje_con_puntos("Agrupando filas")

        filas_agrupadas = self.agrupar_filas()

        mostrar_mensaje_con_puntos("Sumando filas")

        resultado = Matriz("Matriz Reducida", len(filas_agrupadas), self.m)

        for idx, grupo in enumerate(filas_agrupadas):
            for j in range(1, self.m + 1):
                suma = sum(int(otra_matriz.obtener_dato(i, j)) for i in grupo)
                resultado.datos[(idx + 1, j)] = suma

        return resultado

    def exportar_a_xml(self, ruta):
        root = ET.Element(
            "matriz",
            nombre=self.nombre,
            n=str(self.n),
            m=str(self.m),
            g=str(len(self.agrupar_filas())),
        )
        for (x, y), valor in self.datos.items():
            dato = ET.SubElement(root, "dato", x=str(x), y=str(y))
            dato.text = str(valor)
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
        time.sleep(1)
    print()
