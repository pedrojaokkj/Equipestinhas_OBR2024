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

    print("Conferindo Intercecção...")

    bz = robo.bz
    bz.straight(-50)

    #alinhar o robô
    while robo.sensorCorEsquerda.reflection() > 15:
        bz.drive(0, 80)

    bz.stop()
    bz.turn(-10)

    bz.straight(50)

    cores = confirmaCor()

    if cores == (robo.Color.BLACK, robo.Color.BLACK):
        doisPretos()
    elif cores == (robo.Color.GREEN, robo.Color.GREEN):
        becoSemSaida()
    elif cores == (robo.Color.BLACK, robo.Color.GREEN):
        verde(robo.sensorCorDireita)
    elif cores == (robo.Color.GREEN, robo.Color.BLACK):
        verde(robo.sensorCorEsquerda)