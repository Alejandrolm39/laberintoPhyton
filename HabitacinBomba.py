#!/usr/bin/python
#-*- coding: utf-8 -*-

from Pared import Pared
from HabitacinBomba import HabitacinBomba
from Habitación import Habitación

class HabitacinBomba(Pared, HabitacinBomba, Habitación):
    def __init__(self):
        self.activa = None

