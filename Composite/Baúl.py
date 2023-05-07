#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.Contenedor import Contenedor

class Baul(Contenedor):
    
    def entrar(self):
        return "Has abierto el baúl"

    def esBaul(self):
        return true

    def __str__(self):
        hijos = ''
        for hijo in self.hijos:
            hijos += str(hijo)
    
        return ('Hay un baúl y dentro podemos encontrar: ' + hijos)
