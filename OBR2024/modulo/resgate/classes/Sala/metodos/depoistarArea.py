#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from .....robo  import robo


from ...robo.classeRobo import Robo
from ...Coordenada.coordenada import Coordenada
from ...Mapa.mapa import Mapa
from ...Direcao.direcao import Direcao

from ....movimentos.depositar import depositar


def depositarArea(self, area : Coordenada):
    #Implementação do método depositarArea

    
    maxY = len(self._mapa.coordenadas[0]) - 1
    maxX = len(self._mapa.coordenadas) - 1

    quinas = [self._mapa.coordenadas[0][0], self._mapa.coordenadas[0][maxY], self._mapa.coordenadas[maxX][maxY], self._mapa.coordenadas[maxX][0]]


    if area == quinas[0]:
        direcaoAlvo =  Direcao('direita')
        coordenadaAlvo = self._mapa.coordenadas[1][1] 

    elif area == quinas[1]:
        direcaoAlvo =  Direcao('tras')
        coordenadaAlvo = self._mapa.coordenadas[1][maxY - 1]

    elif area == quinas[2]:
        direcaoAlvo =  Direcao('esquerda')
        coordenadaAlvo = self._mapa.coordenadas[maxX - 1][maxY- 1]

    elif area == quinas[3]:
        direcaoAlvo =  Direcao('frente')
        coordenadaAlvo = self._mapa.coordenadas[maxX - 1][1]

    self.enviarRobo(coordenadaAlvo, direcaoAlvo)
    
    robo.bz.reset()

    robo.bz.turn(-45)

    depositar(True)

    robo.bz.straight(-robo.bz.distance())

    robo.bz.turn(45)
    

    


