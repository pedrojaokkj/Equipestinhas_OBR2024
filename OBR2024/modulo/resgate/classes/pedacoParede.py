#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo
from .parede import Parede
from .direcao import Direcao

class PedacoDeParede:
    def __init__(self, parede : Parede, parte: int, aberta = None) -> None:
        '''Cria uma Instancia do objeto

        Parameters:
            parede(Parede) : Parede onde o pedaço se encontra
            parte : Coluna onde o robô se encontra
        '''


        self._parede = parede
        self._parte = parte
        self._aberta = aberta

        if parede.valor.casefold() == 'a':
            self._direcao = Direcao('baixo')
        elif parede.valor.casefold() == 'b':
            self._direcao = Direcao('esquerda')
        elif parede.valor.casefold() == 'c':
            self._direcao = Direcao('cima')
        elif parede.valor.casefold() == 'd':
            self._direcao = Direcao('direita')
        