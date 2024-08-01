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

    robo.bizzoru.straight(95)

    while True:
        robo.bizzoru.drive(0, 90 *lado)  
        if outroSensor.reflection <= 40:
            robo.bizzoru.stop()
            break


    while True:
        robo.bizzoru.drive(0, -90 * lado)  
        if sensor.reflection <= 40:
            robo.bizzoru.stop()
            break    

    robo.bizzoru.stop()

    #implementar ajustes
    