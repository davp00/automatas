from grafos.arista import *


class Vertice:
    def __init__(self, valor):
        self.aristas = []
        self.valor = valor

    def relacionar(self, valor, vertice):
        arista = Arista(valor, vertice)
        self.aristas.append(arista)

    def mostrar_relaciones(self):
        for arista in self.aristas:
            print("{} -> {} -> {}".format(self.valor, arista.valor, arista.vertice.valor))