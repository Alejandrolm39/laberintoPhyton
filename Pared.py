#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    def entrar(alguien):
        return "Te has chocado con un pared"
    
    def esPared(self):
        return true