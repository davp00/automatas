from tkinter import *
from automatas.automata import Automata
from componentes.input import Input
import re


class VentanaPrincipal:  # ▲(q0)={(q1,a)}

    ruta_img = "out/process.gv.png"

    def __init__(self):
        self.root = Tk()
        self.frame = Frame(self.root)
        self.frame.config(width=600, height=600)
        self.root.geometry("600x600")
        self.automata = Automata()
        self.iniciar_componentes()
        self.frame.pack()
        self.root.mainloop()

    def iniciar_componentes(self):
        self.input_estados = Input(self.frame)
        self.input_estados.place(x=180, y=10)

        self.btn_enviar = Button(self.frame, text="Enviar", command=self.click_btn_enviar)
        self.btn_enviar.place(x=320, y=8)

        Label(self.frame, text="Ingrese el estado: ").place(x=80, y=10)

        self.img_automata = PhotoImage(file=self.ruta_img)
        self.label_img = Label(self.root, image=self.img_automata)
        self.label_img.place(x=10, y=200)

    def click_btn_enviar(self):
        txt_input_estados = self.input_estados.get()
        if self.verticar_cadena(txt_input_estados):
            self.actualizar_automata(self.extraer_estados(txt_input_estados))
        else:
            print("ERROR: En la cadena")
        self.input_estados.set_text("")
        self.automata.show()
        self.actualizar_imagen()

    def actualizar_automata(self, estados):
        self.automata.nuevo_estado(estados[0][0])
        i = 1
        while i < len(estados):
            estado = self.automata.buscar(estados[i][0], self.automata.estados)
            if estado is None:
                self.automata.nuevo_estado(estados[i][0])
            self.automata.nueva_relacion(estados[0][0], estados[i][0], estados[i][1])
            i += 1

        self.automata.mostrar_relaciones(self.automata.estados)

    def actualizar_imagen(self):
        self.img_automata.config(file=self.ruta_img)

    @staticmethod
    def verticar_cadena(cadena):
        pattern = re.compile("^(▲)[(]([a-zA-Z]([0-9]+))([,][a-zA-Z])?[)]"  # estado principal
                             "[=][{]([(]([a-zA-Z]([0-9]+))([,][a-zA-Z])[)])"  # estado a relacionar
                             "([,][(]([a-zA-Z]([0-9]+))([,][a-zA-Z])?[)])*[}]$")
        return pattern.search(cadena)

    @staticmethod
    def extraer_estados(cadena):
        pattern = re.compile("[(]([a-zA-Z]([0-9]+))([,][a-zA-Z])?[)]")
        estados = []
        for est in pattern.finditer(cadena):
            tupla = est.span()
            estado = cadena[tupla[0]:tupla[1]]
            estado = estado.replace('(', '')
            estado = estado.replace(')', '')
            estado = estado.split(',')
            estados.append(estado)
        return estados


ventana = VentanaPrincipal()