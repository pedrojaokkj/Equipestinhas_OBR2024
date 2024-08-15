#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo
from .parede import Parede

class AreaDeResgate:
    def __init__(self, paredeE : Parede, paredeD : Parede) -> None:
        self._paredeEsqueda = paredeE
        self._paredeDireita = paredeD 