from grafos.grafo import Grafo
from automatas.estado import Estado
from graphviz import Digraph
import os


os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/graphviz-2.38/release/bin/'


class Automata(Grafo):
    def __init__(self):
        super().__init__()
        self.estados = []
        self.d = Digraph('Automata', filename='out/process.gv', engine='sfdp', format="png")
        self.d.attr(rankdir='LR', size='8,5')
        self.d.render()

    def nuevo_estado(self, valor):
        estado = Estado(valor)
        self.estados.append(estado)

    def nueva_relacion(self, est1, est2, valor):
        estado1 = self.buscar(est1, self.estados)
        estado2 = self.buscar(est2, self.estados)

        if estado1 is not None and estado2 is not None:
            estado1.relacionar(valor, estado2)
        else:
            print("ERROR: ALGUNO DE LO ESTADOS NO EXISTE")

    def show(self):
        self.d.clear()
        self.d.attr(rankdir='LR', size='8,5')
        self.d.attr('node', shape='doublecircle')
        #self.estados[0].set_final(True)
        '''for estado in self.estados:
            if estado.final is True:
                self.d.node(estado.valor)'''

        self.d.attr('node', shape='circle')
        for estado in self.estados:
            for arista in estado.aristas:
                self.d.edge(estado.valor, arista.vertice.valor, label=arista.valor)

        self.d.render()