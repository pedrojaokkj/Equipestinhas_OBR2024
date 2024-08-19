#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo

def giro_direita(x:float):
    
    bz = robo.bz
    n = 90

    print('Giro pra direita')
    bz.turn(n*x)