#!/usr/bin/python
#-*- coding: utf-8 -*-

from Juego import Juego

class Playground():
    
if __name__=="__main__":
    juego = Juego()
    juego.laberinto4HabitacionesFMDC()
    print(str(juego.laberinto))
    print(str(juego.laberinto.obtenerHijo(1)))
    print(str(juego.laberinto.obtenerHijo(2)))
    print(str(juego.laberinto.obtenerHijo(2).obtenerHijo(1)))
    print(str(juego.laberinto.obtenerHijo(3)))
    print(str(juego.laberinto.obtenerHijo(4)))
