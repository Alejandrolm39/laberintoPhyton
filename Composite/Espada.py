#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.Hoja import Hoja

class Espada(Hoja):
    def entrar(alguien):
        return "Te has encontrado una espada y te has cortado"
    
    def esEspada(self):
        return True

    def __str__(self):
        return ('Hay una espada')
