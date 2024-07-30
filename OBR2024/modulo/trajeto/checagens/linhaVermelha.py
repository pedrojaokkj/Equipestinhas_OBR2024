#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo

# Verifica se o robô está na linha vermelha
def linhaVermelha():
    if robo.sensorCorDireita.color() == robo.Color.RED and robo.sensorCorEsquerda.color() == robo.Color.RED:
        robo.bizzoru.straight(10)
    retorno = robo.sensorCorDireita.color() == robo.Color.RED and robo.sensorCorEsquerda.color() == robo.Color.RED
    return retorno
