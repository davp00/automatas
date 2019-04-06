from grafos.vertice import *


class Grafo:
    def __init__(self):
        self.__vertices = []

    def nuevo_vertice(self, valor):
        vertice = Vertice(valor)
        self.__vertices.append(vertice)

    @staticmethod
    def buscar(valor, vertices):
        for vertice in vertices:
            if vertice.valor == valor:
                return vertice

    def crear_relacion(self, v1, v2, valor):
        vertice1 = self.buscar(v1, self.__vertices)
        vertice2 = self.buscar(v2, self.__vertices)

        if vertice1 is not None and vertice2 is not None:
            vertice1.relacionar(valor, vertice2)
        else:
            print("ERROR: PUEDE QUE ALGUNO DE LOS VERTICES NO EXISTA")

    @staticmethod
    def mostrar_relaciones(vertices):
        for vertice in vertices:
            vertice.mostrar_relaciones()

    def ver_relaciones(self):
        self.mostrar_relaciones(self.__vertices)