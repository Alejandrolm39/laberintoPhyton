#!/usr/bin/python
#-*- coding: utf-8 -*-

from Laberinto import Laberinto
from ElementoMapa import ElementoMapa

class Habitacion(ElementoMapa):
    def __init__(self, num):
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.num =num

    def entrar(alguien):
        return "Estas en la habitacion " + self.num

    def esHabitacion(self):
        return True