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

    if sensor == robo.sensorCorDireita:
        lado = 1
        motor = robo.motorDireito
        motor2 = robo.motorEsquerdo 
        outroSensor = robo.sensorCorEsquerda
    else:
        lado = -1
        motor = robo.motorEsquerdo
        motor2 = robo.motorDireito
        outroSensor = robo.sensorCorDireita

    robo.bz.straight(103)

    robo.bz.turn(20 * lado)
    robo.bz.stop()
    
    motor2.run(200)
    motor.run(-200) 
    while True:

        if outroSensor.reflection() <= 40:
            motor2.stop()
            motor.stop()
            break


    while True:
        motor.run(100)
        motor2.run(-100)
        if sensor.reflection() <= 40:
            robo.bz.stop()
            break    

    robo.bz.turn(13)


    