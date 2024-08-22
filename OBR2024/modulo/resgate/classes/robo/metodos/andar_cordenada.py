#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from .....robo import robo

def andar_cordenada(self, x:int):
    
    bz = robo.bz
    cm = 300
    direcao = self._direcaoAtual
    coordenada = self._coordenadaAtual

    print('Andando uma coordenada')
    print('Direcionando para o meio do ladrilho')
    bz.straight(cm*x)


    
