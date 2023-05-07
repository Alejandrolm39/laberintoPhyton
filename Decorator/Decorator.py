#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.ElementoMapa import ElementoMapa
from abc import ABC, abstractclassmethod
from Composite.Hoja import Hoja

class Decorator(ElementoMapa):
    def __init__(self):
        component = None

    def component(self):
        return self
