#!/usr/bin/python
#-*- coding: utf-8 -*-

from Strategy.Orientacion import Orientacion

class Norte(Orientacion):
    
    def ponerElementoEn(self, elm, hab):
        hab.este = elm
