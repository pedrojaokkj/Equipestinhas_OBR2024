#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ..robo import robo
from .classes.Sala.classeSala import SalaDeResgate
from .classes.robo.classeRobo import Robo
from .classes.Coordenada.coordenada import Coordenada
from .classes.Direcao.direcao import Direcao


# Execução do Resgate
def resgate():


    print(robo.bz.distance())
    robot = Robo()

    print("Criando Instância de Sala...")

    sala = SalaDeResgate(robot)

    sala.encontrarAreas()

    sala.sair()

    
    robo.wait(5000)


