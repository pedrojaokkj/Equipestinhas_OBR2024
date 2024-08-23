#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ..robo.classeRobo import Robo
from ..Coordenada.coordenada import Coordenada
from ..Mapa.mapa import Mapa
from ..Direcao.direcao import Direcao
from .funcoesConstrutoras.iniciarMapa import iniciarMapa
from .metodos.andar_cordenada import andar_cordenada

from .metodos.enviarRobo import enviarRobo

class SalaDeResgate:

    def __init__(self, roboObj : Robo) -> None:
        '''Cria uma Instancia do objeto

        Parameters:
            robo(Robo): robo que entrou na sala de resgate
        '''
        
        self._entrada = [Coordenada(x = 0, y=1), Direcao('tras')]
        self._saida = [Coordenada(x = 0, y=0), Direcao(None)]
        self._robo, self._mapa = iniciarMapa(self, roboObj, Mapa())
        


    #atribuição das funções da classe
    
    def andarCoordenada(self):
        andar_cordenada(self)

    def enviarRobo(self, coordenada : Coordenada, direcao : Direcao) -> None:
        enviarRobo(self, coordenada, direcao)


    def encontrarAreas():
        print('Procurando áreas...')
        

    
            












        
    
