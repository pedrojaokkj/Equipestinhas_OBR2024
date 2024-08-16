#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ....robo import robo
from ...checagens.confirmaCor import confirmaCor
from .doisPretos import doisPretos
from .becoSemSaida import becoSemSaida
from .verde import verde


def becoOuDoisPretos():
    '''Confere se o robô está em uma intercecção comum ou em um beco sem saída e chama a função apropriada.
    
    '''

    print("Conferindo Intercecção(beco ou dois pretos)...")


    bz = robo.bz
    bz.stop()
    bz.straight(40)

    bz.straight(-40)

    if robo.sensorCorDireita.reflection() > 60 or robo.sensorCorEsquerda.reflection() > 60:
        return
    bz.straight(-40)

    

    #alinhar o robô

    while robo.sensorCorEsquerda.reflection() > 15:
        robo.bz.drive(0, 40)

    robo.bz.stop()

    while robo.sensorCorEsquerda.reflection() <= 15:
        robo.bz.drive(0, -40)

    robo.bz.stop()

    bz.turn(-7)

    robo.bz.reset()

    while robo.sensorCorEsquerda.reflection() > 15 and robo.sensorCorDireita.reflection() > 15 and robo.bz.distance() >=40:
        robo.bz.drive(35, 0)
    
    print(robo.bz.distance())
    bz.stop()


    cores = confirmaCor()

    if cores == (robo.Color.BLACK, robo.Color.BLACK):
        doisPretos()
    elif cores == (robo.Color.GREEN, robo.Color.GREEN):
        becoSemSaida()
    elif cores == (robo.Color.BLACK, robo.Color.GREEN):
        verde(robo.sensorCorDireita)
    elif cores == (robo.Color.GREEN, robo.Color.BLACK):
        verde(robo.sensorCorEsquerda)