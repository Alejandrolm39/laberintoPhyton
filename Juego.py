#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.Laberinto import Laberinto
from Composite.Habitacion import Habitacion
from Composite.Puerta import Puerta
from Composite.Pared import Pared
from Decorator.Bomba import Bomba
from Decorator.Fuego import Fuego
from Composite.Espada import Espada
from Composite.Baul import Baul

class Juego():
    def __init__(self):
        self.laberinto = None

    def fabricarPared(self):
        return Pared()

    def fabricarNorte(self):
        return Norte()

    def fabricarSur(self):
        return Sur()

    def fabricarEste(self):
        return Este()

    def fabricarOeste(self):
        return Oeste()

    def fabricarEspada(self):
        return Espada()

    def fabricarBaulEn(self, unCont):

        un_num = len(un_cont.hijos) + 1

        arm = Baul(un_num)
        arm.ponerEn(self.fabricarNorte(), self.fabricarPared())
        arm.ponerEn(self.fabricarOeste(), self.fabricarPared())
        arm.ponerEn(self.fabricarEste(), self.fabricarPared())

        arm.agregarOrientacion(self.fabricarNorte())
        arm.agregarOrientacion(self.fabricarSur())
        arm.agregarOrientacion(self.fabricarEste())
        arm.agregarOrientacion(self.fabricarOeste())

        puerta = self.fabricarPuerta(arm, un_cont)
        arm.ponerEn(self.fabricarSur(), puerta)

        un_cont.agregarHijo(arm)

    def fabricarBomba(self):
        return Bomba()

    def fabricarFuego(self):
        return Fuego()

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

    def laberinto4HabitacionesFMDC(self):
        self.laberinto = self.fabricarLaberinto

        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)

        
        b1 = self.fabricarBaulEn(hab3)
        b2 = self.fabricarBaulEn(hab2)

        bm1 = self.fabricarBomba()
        bm1.component = self.fabricarPuerta(hab3, hab4)
        bm1.activar()

        bm2 = self.fabricarBomba()
        bm2.activar()

        b1.agregarHijo(self.fabricarEspada())
        b2.agregarHijo(bm2)

        fuego = self.fabricarFuego()

        puerta1 = self.fabricarPuerta(hab1, hab2)
        puerta1.abrir()
        puerta2 = self.fabricarPuerta(hab2, hab4)   
        puerta2.abrir()
        #puerta3 = self.fabricarPuerta(hab3, hab4)
        puerta4 = self.fabricarPuerta(hab1, hab3)

        n = fabricarNorte()
        s = fabricarSur()
        e = fabricarEste()
        o = fabricarOeste()

        hab1.ponerEn(n, self.fabricarPared())
        hab1.ponerEn(e, puerta1)
        hab1.ponerEn(o, self.fabricarPared())
        hab1.ponerEn(s, puerta4)

        hab2.ponerEn(s, puerta2)
        hab2.ponerEn(e, self.fabricarPared())
        hab2.ponerEn(o, puerta1)
        hab2.ponerEn(n, self.fabricarPared())

        hab3.ponerEn(n, puerta4)
        hab3.ponerEn(s, self.fabricarPared())
        hab3.ponerEn(e, bm1)
        hab3.ponerEn(o, self.fabricarPared())

        hab4.ponerEn(n, puerta2)
        hab4.ponerEn(e, self.fabricarPared())
        hab4.ponerEn(o, bm1)
        hab4.ponerEn(s, self.fabricarPared())
        fuego.component = hab4

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)


