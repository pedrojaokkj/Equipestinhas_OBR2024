#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo

def giro_esquerda(x:int):

    bz = robo.bz
    n = 90

    print('Giro pra esquerda')
    bz.turn(n*x)