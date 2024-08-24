#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ....robo import robo
from ...checagens.alinhar import alinhar

def verde(sensor:robo.ColorSensor):
    '''Vira o Robô de acordo com a marcação verde das intercecções.
    
    Parameters:
        sensor (ColorSensor) : Sensor que detectou a cor verde
    '''
    print('Verde no {}'.format(sensor))

    robo.bz.stop()

    if sensor == robo.sensorCorDireita:
        lado = 1
        motor = robo.motorDireito
        motor2 = robo.motorEsquerdo 
        sensor2 = robo.sensorCorEsquerda
    else:
        robo.ev3.light.on(robo.Color.RED)
        lado = -1
        motor = robo.motorEsquerdo
        motor2 = robo.motorDireito
        sensor2 = robo.sensorCorDireita

    robo.bz.straight(75)

    robo.bz.turn(35 * lado)
    robo.bz.stop()

    print("Procurando Linha...")

    while sensor2.reflection() > 15:
        robo.bz.drive(0, 40 * lado)

    robo.bz.stop()


    alinhar()

    robo.ev3.light.off()
    