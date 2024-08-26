from classes.Nodo import Nodo


class Circular_List:
    def __init__(self):
        self.cabeza = None

    def agregar(self, matriz_info):
        nuevo_nodo = Nodo(matriz_info)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cabeza.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza

    def exists(self, nombre):
        if not self.cabeza:
            return False
        actual = self.cabeza
        while True:
            if actual.matriz.nombre == nombre:
                return True
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return False

    def __iter__(self):
        nodo_actual = self.cabeza
        if not nodo_actual:
            return
        yield nodo_actual.matriz
        nodo_actual = nodo_actual.siguiente
        while nodo_actual != self.cabeza:
            yield nodo_actual.matriz
            nodo_actual = nodo_actual.siguiente
