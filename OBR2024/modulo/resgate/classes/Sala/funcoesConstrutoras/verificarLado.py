#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo

def verificarLado() -> bool:
    ''' verifica se tem parede no lado esquerdo do robô.

    Returns:
        Parede(bool) : True se o sensor detectar parede na esquerda. 
    '''

    print('Detectando parede na esquerda...')

    parede = False
    leituras = []

    robo.bz.reset()
    #vai pra frente armazenando as leituras
    while robo.bz.distance() < 30:
        robo.bz.drive(20,0)
        leituras.append(robo.ultrassonicoLado.distance())
        robo.wait(1)


    robo.bz.stop()
    distancia = robo.bz.distance()
    robo.bz.reset()


    #volta armazenando as leituras
    while robo.bz.distance() > -distancia:
        robo.bz.drive(-20,0)
        leituras.append(robo.ultrassonicoLado.distance())
        robo.wait(1)

    robo.bz.stop()

    media = sum(leituras) / len(leituras)
    parede = media < 100
    print('Parede : ', parede)

    robo.bz.turn(2)

    return parede