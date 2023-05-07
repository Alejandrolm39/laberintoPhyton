#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator.Decorator import Decorator

class Bomba(Decorator):

    def __init__(self):
        self.activa = False

    def activar(self):
        self.activa = True
        return "Bomba activada"

    def desactivar(self):
        self.activa = False 
        return "Bomba desactivada"

    def entrar(self):
        if activa == True:
            return "La bomba ha explotado"
            activa = False
        else:
            super().entrar()

    def esBomba(self):
        return True

    def __str__(self):
         return "Soy una bomba que decora -> " + str(self.component)
    
