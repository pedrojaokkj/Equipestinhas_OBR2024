#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo
from .parede import Parede
from .direcao import Direcao
from coordenada import Coordenada

class PedacoDeParede:
    def __init__(self, parede : str, parte: int = 0, coordenada : Coordenada = Coordenada(), aberta = None) -> None:
        '''Cria uma Instancia do objeto

        Parameters:
            parede(Parede) : Parede onde o pedaço se encontra
            parte : Coluna onde o robô se encontra
            coordenada(Coordenada) : Posicao da parede
        '''
        if not isinstance(parede, str) or parede.casefold() in ['a', 'b', 'c', 'd'] == False:
            raise ValueError("parede deve ser uma string 'a', 'b', 'c', 'd'")
        
        self._parede = parede.casefold()
        self._parte = parte
        self._aberta = aberta
        self._coordenada = coordenada


        if parede.casefold() == 'a':
            self._direcao = Direcao('baixo')
        elif parede.casefold() == 'b':
            self._direcao = Direcao('esquerda')
        elif parede.casefold() == 'c':
            self._direcao = Direcao('cima')
        elif parede.casefold() == 'd':
            self._direcao = Direcao('direita')

        
        
    @property
    def coordenada(self):
        return self._coordenada




    @coordenada.setter
    def coordenada(self, coordenada : Coordenada):
        if not isinstance(coordenada, Coordenada):
            raise ValueError("coordenada deve ser uma string do tipo Coordenada")
        self._coordenada = coordenada
        