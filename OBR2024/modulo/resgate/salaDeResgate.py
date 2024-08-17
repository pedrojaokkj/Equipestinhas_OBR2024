#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ..robo.robo import robo
from .classes.Sala.classeSala import SalaDeResgate
from ..robo.classeRobo import Robo


# Execução do Resgate
def resgate():
    print("Alinhando...")
    #alinhar

    print("Criando Instância de Sala...")
    Sala = SalaDeResgate(robo)

