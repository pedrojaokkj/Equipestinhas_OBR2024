#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ....robo import robo

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
        lado = -1
        motor = robo.motorEsquerdo
        motor2 = robo.motorDireito
        sensor2 = robo.sensorCorDireita

    robo.bz.straight(80)

    robo.bz.turn(35 * lado)
    robo.bz.stop()

    print("Procurando Linha...")

    while sensor2.reflection() > 15:
        robo.bz.drive(0, 40 * lado)

    robo.bz.stop()

    while sensor2.reflection() <= 35:
        robo.bz.drive(0, -40 * lado)


    robo.bz.stop()
    robo.bz.turn(-5 * lado) 
    robo.bz.straight(-15)
    robo.bz.stop()

    