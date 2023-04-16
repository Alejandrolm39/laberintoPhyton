#!/usr/bin/python
#-*- coding: utf-8 -*-

class Juego():
    def __init__(self):
        self.laberinto = None

    def fabricarPared(self):
        return Pared()

    def fabricarHabitacion(self, numero):
        habitacion = Habitacion()
        habitacion.num = numero

        return habitacion

    def fabricarLaberinto(self):
        return laberinto()

    def fabricarPuerta(self, lado1, lado2):
        puerta = Puerta()
        puerta.lado1 = lado1
        puerta.lado2 = lado2

        return puerta

    def laberinto2HabitacionesFM(self):
        laberinto = self.fabricarLaberinto

        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        
        puerta = self.fabricarPuerta(hab1, hab2)

        hab1.norte = self.fabricarPared
        hab1.este = self.fabricarPared
        hab1.oeste = self.fabricarPared

        hab2.sur = self.fabricarPared
        hab2.este = self.fabricarPared
        hab2.oeste = self.fabricarPared

        hab1.sur = puerta
        hab2.norte = puerta

        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)

