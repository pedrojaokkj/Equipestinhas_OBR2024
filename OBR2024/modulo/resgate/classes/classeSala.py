#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo.robo import robo
from .pedacoParede import PedacoDeParede
from.parede import Parede
from ...robo.classeRobo import Robo 
from .funcoes.escanearSala import escanearSala
from .coordenada import Coordenada

class SalaDeResgate:

    def __init__(self, robo : Robo) -> None:
        '''Cria uma Instancia do objeto

        Parameters:
            robo(Robo): robo que entrou na sala de resgate
        '''


        self._robo = robo
        self._coordenadaAtual = Coordenada()
        self._largura, self._comprimento, self._entrada, self._saida = escanearSala() 
        
    
    