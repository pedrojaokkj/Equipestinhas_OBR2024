#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ....robo import robo

def preto(sensor:robo.ColorSensor):
    '''Segue o protocolo para quando um sensor detecta preto.
    
    Parameters:
        sensor (ColorSensor) : Sensor que detectou a cor preta
    '''

    print("Função Preto")

    robo.bz.stop()

    if sensor == robo.sensorCorDireita:
        motor = robo.motorDireito
        outroMotor = robo.motorEsquerdo
        outroSensor = robo.sensorCorEsquerda
    else:
        motor = robo.motorEsquerdo
        outroMotor = robo.motorDireito
        outroSensor = robo.sensorCorDireita


    if sensor.reflection() <= 8:
        print("virar")

    else:
        print("ajustar")        
    