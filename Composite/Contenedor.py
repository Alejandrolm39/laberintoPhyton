#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.ElementoMapa import ElementoMapa

class Contenedor(ElementoMapa):
    def __init__(self):
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.hijos = list()
        self.orientaciones = list()

    def agregarHijo(self, elementoMapa):
        
        elementoMapa.padre = self
        self.hijos.append(elementoMapa)

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)

    def ponerEn(self, una_or, un_em):
        una_or.ponerElementoEn(un_em, self)

    def obtenerHijo(self,num):
        for hijo in self.hijos:
            if hijo.num == num:
                return hijo




