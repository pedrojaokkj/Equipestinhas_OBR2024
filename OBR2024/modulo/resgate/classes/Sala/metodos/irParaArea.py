#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________

from ...Direcao.direcao import Direcao
from ...Coordenada.coordenada import Coordenada
from modulo.robo import robo
from ...robo.classeRobo import Robo
from modulo.resgate.classes.robo.metodos.checarParedeouArea import checarParedeouArea
from modulo.resgate.classes.robo.metodos.capturar import captura
from modulo.resgate.movimentos.depositar import depositar

def irParaArea():
    bz = robo.bz
    bz.reset()
    bz.turn(45)
    bz.reset()
    
    bz.straight(80)
    captura()

    while robo.ultrassonicoFrente.distance() > 65:
        bz.drive(100,0)
    bz.stop()
    
    distancia = robo.bz.distance()
    
    area = checarParedeouArea()

    if area == True:
            bz.turn(180)
            depositar(True)
            bz.straight(50)
            bz.turn(180)
            bz.straight(100)

    while robo.ultrassonicoFrente.distance() < 65:
        bz.drive(100,0)
    bz.stop()

    bz.straight(-distancia)
    bz.turn(-45)

    return area

    





