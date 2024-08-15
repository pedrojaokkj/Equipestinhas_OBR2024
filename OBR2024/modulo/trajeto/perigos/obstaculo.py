#!/usr/bin/env pybricks-micropython

from ...robo import robo

# Desvia do obstáculo
def obstaculo():
    
    print("detectando o obstaculo")
    robo.bz.turn(90)


    print('sensores detectam o preto da linha( antes do obstaculo)')        
    while robo.sensorCorEsquerda.color() != robo.Color.BLACK:
        robo.bz.drive(-100,0)
    robo.bz.stop()

    print('contornando obstaculo')
    while robo.ultrassonicoLado.distance() < 150:
        robo.bz.drive(100,0)
    robo.bz.stop()

    robo.bz.straight(160)
    robo.bz.turn(-90)

    while robo.ultrassonicoLado.distance() > 150:
            robo.bz.drive(100,0)
    robo.bz.stop()

    robo.wait(700)

    robo.bz.straight(10)

    while robo.ultrassonicoLado.distance() < 200:
        robo.bz.drive(100,0)
    robo.bz.stop()

    robo.wait(700)

    robo.bz.straight(180)
    robo.bz.turn(-90)

    print('voltando para a linha(depois do obstaculo)')
    print('sensores detectam o preto da inha(depois do obstaculo)')
    while robo.sensorCorEsquerda.color() and robo.sensorCorDireita.color() != robo.Color.BLACK:
        robo.bz.drive(100,0)
    robo.bz.stop()

    robo.wait(700)

    print('robo se ajusta na linha')
    while robo.sensorCorEsquerda.color() and robo.sensorCorDireita.color() == robo.Color.BLACK:
        robo.bz.drive(100,0)
    robo.bz.stop()

    robo.bz.straight(40)
    robo.bz.turn(90)
    
                        
                             
                        



