#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo
from modulo.trajeto.perigos.interceccoes.preto import preto

def teste():
    while True:
        robo.bz.drive(200, 0)