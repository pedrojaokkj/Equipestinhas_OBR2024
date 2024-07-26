#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo

def verde(sensor:robo.ColorSensor):
    if sensor == robo.sensorCorDireita:
        lado = 1
        outroSensor = robo.sensorCorEsquerda
    else:
        lado = -1
        outroSensor = robo.sensorCorDireita

    robo.meuRobo.straight(60)

    while outroSensor.color == robo.Color.WHITE:
        robo.meuRobo.drive(20, 50 * lado)
    robo.meuRobo.stop()

    while sensor == robo.Color.WHITE:
        robo.meuRobo.drive(20, 50* lado * -1)
    robo.meuRobo.stop()

    #implementar ajustes
    