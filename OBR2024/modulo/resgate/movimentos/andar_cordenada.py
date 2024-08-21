#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo

def andar_cordenada(x:int):
    
    bz = robo.bz
    cm = 300
    
    print('Andando uma coordenada')
    print('Direcionando para o meio do ladrilho')
    bz.straight(cm*x)


    
