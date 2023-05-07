#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    def entrar(alguien):
        return "Te has chocado con un pared"
    
    def esPared(self):
        return True

    def __str__(self):
        return "Una pared"