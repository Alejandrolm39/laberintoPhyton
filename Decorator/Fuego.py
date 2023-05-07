#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator.Decorator import Decorator

class Fuego(Decorator):
    
    def __init__(self):
        self.encendido = False

    def encender(self):
        self.encendido = True
        return "Fuego encendido"

    def desactivar(self):
        self.encendido = False 
        return "Fuego encendido"

    def entrar(self):
        if encendido == True:
            return "Te has quemado"
            encendido = False
        else:
            super().entrar()

    def esFuego(self):
        return True

    def __str__(self):
            return "Soy un fuego que decora -> " + str(self.component)