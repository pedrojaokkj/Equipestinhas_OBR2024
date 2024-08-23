#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from .....robo import robo
from ...Direcao.direcao import Direcao
from ...Coordenada.coordenada import Coordenada



def andar_cordenada(self):
    
    bz = robo.bz
    cm = 280
    direcao = self._robo.direcaoAtual
    coordenada = self._robo.coordenadaAtual

    bz.reset()

    print('Andando uma coordenada')
    print('Direcionando para o meio do ladrilho')


    while robo.bz.distance() < cm:
        bz.drive(80, 0)
        if robo.ultrassonicoFrente.distance() < 380 - cm:
            self._robo.capturar

    bz.stop()

    x = coordenada.x -1
    y = coordenada.y -1

    if  direcao == Direcao('tras'):
        coordenada = self._mapa.coordenadas[x][y-1]

    elif direcao == Direcao('frente'):
        coordenada = self._mapa.coordenadas[x][y+1]

    elif direcao == Direcao('direita'):
        coordenada = self._mapa.coordenadas[x+1][y]

    elif direcao == Direcao('esquerda'):
        coordenada = self._mapa.coordenadas[x-1][y]


    if coordenada.explorada == False:
        coordenada.explorada = True
    


    self._robo.coordenadaAtual = coordenada


    
