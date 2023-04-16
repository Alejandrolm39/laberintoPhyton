#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self):
        self.abierta = False
        self.lado1 = None
        self.lado2 = None

    def abrir(self):
        self.abierta = True

    def cerrar(self):
        self.abierta = False

    def esPuerta(self):
        return True

    def estaCerrada(self):
        if self.abierta == False:
            return True
        else:
            return False