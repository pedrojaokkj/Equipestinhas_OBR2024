#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo
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
        
        self._entrada = [Coordenada(x = 0, y=1), Direcao('tras')]
        self._saida = [Coordenada(x = 0, y=0), Direcao(None)]
        self._robo, self._mapa = self.iniciarMapa(roboObj, Mapa())
        



    iniciarMapa = iniciarMapa


    def enviarRobo(self, coordenada : Coordenada, direcao : Direcao):

        mapa = self._mapa
        posicaoAtual = self._robo.coordenadaAtual
        direcaoAtual = self._robo.direcaoAtual
        
        diferencaY = posicaoAtual.y - coordenada.y 


        # while posicaoAtual != coordenada or direcaoAtual != direcao:






        
    