from grafos.vertice import Vertice


class Estado(Vertice):
    def __init__(self, valor):
        super().__init__(valor)
        self.final = False

    def set_final(self, valor):
        self.final = valor