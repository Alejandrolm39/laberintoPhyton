#!/usr/bin/python
#-*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class ElementoMapa(ABC):
    def __init__(self):
        self.padre = None
        self.num = None

    @abstractmethod    
    def entrar(self):
        pass 

    def esHabitacion(self):
        return False

    def esPared(self):
        return False

    def esPuerta(self):
        return False

    def esBaul(self):
        return False

    def esEspada(self):
        return False
