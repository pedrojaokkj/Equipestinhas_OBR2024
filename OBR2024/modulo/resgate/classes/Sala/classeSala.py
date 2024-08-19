#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo.robo import robo
from ..robo.classeRobo import Robo 
from .funcoesConstrutoras.iniciarMapa import iniciarMapa
from ..Coordenada.coordenada import Coordenada
from ..Mapa.mapa import Mapa


class SalaDeResgate:

    def __init__(self, robo : Robo) -> None:
        '''Cria uma Instancia do objeto

        Parameters:
            robo(Robo): robo que entrou na sala de resgate
        '''
        

        self._robo = robo
        self._mapa = self.iniciarMapa(Mapa())



    iniciarMapa = iniciarMapa

        
    
