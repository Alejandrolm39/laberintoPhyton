#!/usr/bin/python
#-*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class ElementoMapa(ABC):
    def __init__(self):
        self.padre = None

    @abstractmethod    
    def entrar(self):
        pass 

    def esHabitacion(self):
        return false

    def esPared(self):
        return false

    def esPuerta(self):
        return false

