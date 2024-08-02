#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ....robo import robo

def verde(sensor:robo.ColorSensor):
    '''Vira o Robô de acordo com a marcação verde das intercecções.
    
    Parameters:
        sensor (ColorSensor) : Sensor que detectou a cor verde
    '''

    if sensor == robo.sensorCorDireita:
        lado = 1
        outroSensor = robo.sensorCorEsquerda
    else:
        lado = -1
        outroSensor = robo.sensorCorDireita

    robo.bz.straight(95)

    while True:
        robo.bz.drive(0, 90 *lado)  
        if outroSensor.reflection <= 40:
            robo.bz.stop()
            break


    while True:
        robo.bz.drive(0, -90 * lado)  
        if sensor.reflection <= 40:
            robo.bz.stop()
            break    

    robo.bz.stop()

    #implementar ajustes
    