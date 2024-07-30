#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo
from .confirmaCor import confirmaCor

# Verifica se o robô está na linha vermelha
def linhaVermelha():
    retorno = False
    if robo.sensorCorDireita.color() == robo.Color.RED and robo.sensorCorEsquerda.color() == robo.Color.RED:
        retorno = confirmaCor() == [robo.Color.RED, robo.Color.RED]
    return retorno
