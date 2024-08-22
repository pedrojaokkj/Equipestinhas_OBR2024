#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo
from ...Coordenada.coordenada import Coordenada
from ...Direcao.direcao import Direcao
from .verificarPadroes import verificar_padroes
from ...robo.classeRobo import Robo


def andarEscaneandoX(robot : Robo, direcao : Direcao):
    saida = (False, None)
    robo.bz.reset()
    parede = False


    distancia = 280 #atribuir
    
    if robo.ultrassonicoFrente.distance() < 100:
        parede = robot.checarParedeouArea()
        print('Checando parede...')

    if parede == False:
        while robo.bz.distance() < distancia:
            robo.bz.drive(60, 0)
            if robo.sensorCorDireita.reflection() < 17:
                print('Saida encontrada')
                saida = (True, direcao)
                
                percorrido = robo.bz.distance()
                robo.bz.straight(-percorrido)
                break

            if robo.bz.distance() > int(distancia / 2):
                if robo.ultrassonicoFrente.distance() < 380 - robo.bz.distance():
                    robot.capturar()
                robo.bz.straight(distancia - robo.bz.distance())
                break 


    



    return Coordenada(y = 2, explorada=True, saida= saida), parede
