#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo.robo import robo
from ..robo.classeRobo import Robo
from .funcoesConstrutoras.iniciarMapa import iniciarMapa
from ..Coordenada.coordenada import Coordenada
from ..Mapa.mapa import Mapa
from ..Direcao.direcao import Direcao

class SalaDeResgate:

    def __init__(self, roboObj : Robo) -> None:
        '''Cria uma Instancia do objeto

        Parameters:
            robo(Robo): robo que entrou na sala de resgate
        '''
        
        self._entrada : list[Coordenada, Direcao] = [Coordenada(x = 0, y=1), Direcao('tras')]
        self._saida : list[Coordenada, Direcao] = [Coordenada(x = 0, y=0), Direcao(None)]
        self._robo : Robo = roboObj
        self._mapa : Mapa = self.iniciarMapa(Mapa())
        



    iniciarMapa = iniciarMapa

        
    
