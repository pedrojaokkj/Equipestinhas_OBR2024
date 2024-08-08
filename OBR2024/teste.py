#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo


def teste():

    while robo.sensorCorEsquerda.reflection() > 15:
        robo.bz.drive(0, 80)

    robo.bz.stop()
    robo.bz.turn(-10)