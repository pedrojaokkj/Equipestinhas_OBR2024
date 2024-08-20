#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ..robo import robo
from .classes.Sala.classeSala import SalaDeResgate
from .classes.robo.classeRobo import Robo


# Execução do Resgate
def resgate():
    robot = Robo(robo.ev3(), robo.bz(), robo.
            motorDireito(), robo.motorEsquerdo(), robo.garra(), robo.mecanismoDeposito(), robo.
            sensorCorEsquerda(), robo.sensorCorDireita(), robo.ultrassonicoLado(), robo.ultrassonicoFrente())

    print("Criando Instância de Sala...")

    sala = SalaDeResgate(robot)


