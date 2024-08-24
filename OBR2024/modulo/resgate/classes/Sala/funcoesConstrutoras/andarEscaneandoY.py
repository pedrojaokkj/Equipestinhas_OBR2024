#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...Coordenada.coordenada import Coordenada
from modulo.robo import robo
from ...Direcao.direcao import Direcao
from ...robo.classeRobo import Robo
from .verificarPadroes import verificar_padroes


def andarEscaneandoY(robot : Robo, y):
    print('Escaneando e andando...')
    robo.bz.reset()
    distancia = 280
    leituras = []
    saida = (False, Direcao(None))
    viuArea = False
    area = False
    ultima = False
    parede = None

    




    while robo.bz.distance() <  distancia:

        robo.bz.drive(100, 0)
        leituras.append(robo.ultrassonicoFrente.distance())
        decrescente, variavel = verificar_padroes(leituras)

        if y == 1  or y == 2 and leituras[0] > 380:

            if robo.bz.distance() > int(distancia / 2):
                if robo.ultrassonicoFrente.distance() < 380 - robo.bz.distance():
                    robot.capturar()
                robo.bz.straight(distancia - robo.bz.distance())
                break 



        elif y == 2 and len(leituras) > 25 :
            
            if viuArea == False:
                robo.bz.straight(75)
                print('Checando area')
                area = robot.checarParedeouArea()
                viuArea = True
                if viuArea == True:
                    robo.bz.straight(-robo.bz.distance())
                else:
                    leituras = []

            else:
                if robo.ultrassonicoFrente.distance() < 380 - robo.bz.distance():
                    robot.capturar()
                robo.bz.straight(distancia - robo.bz.distance())
                break 


            

        if area == True or ultima == True :
            break
                



    coordenada = None
    if ultima == False:
        #corrige a distânccia peercorrida
        if robo.bz.distance() > distancia and area ==  False:
            diferenca = robo.bz.distance() - distancia
            robo.bz.straight(-diferenca)
            
        elif area == True:
            robo.bz.straight(-robo.bz.distance())

        coordenada = Coordenada(x = 0 ,y =  y+1, explorada=True, comArea= viuArea, saida= saida)
        coordenada.exibir_propriedades()
    else:
        print('Fim da linha')

    return coordenada