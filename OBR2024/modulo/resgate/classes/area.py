#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo
from .parede import Parede

class AreaDeResgate:

    def __init__(self, paredeE : Parede, paredeD : Parede) -> None:
        '''Cria uma Instancia do objeto

        Parameters:
            paredeE(Parede) : Parede da esquerda 
            paredeD(Parede) : parede da direita
        '''

        self._paredeEsqueda = paredeE
        self._paredeDireita = paredeD 