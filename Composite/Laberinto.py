#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.ElementoMapa import ElementoMapa

class Laberinto(ElementoMapa):
    
    def __init__(self):

        self.habitaciones = list()

    def agregarHabitacion(self, hab):
        self.habitaciones.append(hab)

    def obtenerHabitacion(self, num):
        return self.habitaciones[num - 1]

    def entrar(self, persona):
        hab = self.obtenerHabitacion(1)
        hab.entrar(persona)

    def __str__(self):
        return "\nBIENVENIDO A NUESTRO LABERINTO"
