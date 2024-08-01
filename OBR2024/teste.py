#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo


def teste(sensor):
    if sensor == robo.sensorCorDireita:
        lado = 1
        outroSensor = robo.sensorCorEsquerda
    else:
        lado = -1
        outroSensor = robo.sensorCorDireita

    robo.bizzoru.straight(60)

    robo.bizzoru.turn(20 * lado)

    while outroSensor.reflection() >= 50:
        robo.bizzoru.drive(20, 50 * lado)
    robo.bizzoru.stop()

    while sensor.reflection() >= 50:
        robo.bizzoru.drive(20, 50* lado * -1)
    robo.bizzoru.stop()