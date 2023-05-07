#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.Laberinto import Laberinto
from Composite.Contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self, num):
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.num = num

    def entrar(alguien):
        return "Estas en la habitacion " + self.num

    def esHabitacion(self):
        return True

    def __str__(self):
            return ("\n\nHabitación número: " + str(self.num) +
        "\n En el norte tenemos: " + str(self.norte) +
        "\n En el norte tenemos: " + str(self.sur) +
        "\n En el norte tenemos: " + str(self.este) +
        "\n En el norte tenemos: " + str(self.oeste))