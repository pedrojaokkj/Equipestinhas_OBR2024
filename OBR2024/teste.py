#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo


def teste():
    while True:
        print(robo.sensorCorDireita.color() == robo.Color.RED)