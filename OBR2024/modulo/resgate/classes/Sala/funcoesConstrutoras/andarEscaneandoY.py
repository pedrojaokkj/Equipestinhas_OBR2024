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
    distancia = 300
    leituras = []
    saida = (False, Direcao(None))
    area = False
    ultima = False
    parede = None

    robot.capturar()
    




    while robo.bz.distance() <  distancia:

        robo.bz.drive(60, 0)
        leituras.append(robo.ultrassonicoFrente.distance())
        decrescente, variavel = verificar_padroes(leituras)

        if y == 1 and robo.ultrassonicoFrente.distance() < 380 - robo.bz.distance() or y == 2 and leituras[0] > 380:

            print("capturar")
            robo.bz.straight(distancia/2)
            robot.capturar()
            robo.bz.stop()
            robo.bz.straight(distancia - robo.bz.distance())
            


        elif y == 2 and len(leituras) > 25:
            
            if variavel:
                #verificar se area
                print('verificando area')

            else:
                print("capturar")
                robo.bz.straight(distancia/2)
                robot.capturar()
                robo.bz.stop()
                robo.bz.straight(distancia - robo.bz.distance())


            

        elif y == 3:


            if parede == None:
                parede = robot.checarParedeouArea()
                
                print('checar parede')

            if parede == True:
                robo.bz.straight(-robo.bz.distance())
                ultima = True

            elif len(leituras) > 25:

                if robo.sensorCorDireita.reflection() < 15:
                    saida = (True, Direcao('Frente'))
                    robo.bz.straight(-robo.bz.distance())
                    ultima = True

                elif variavel:

                    area = robot.checarParedeouArea()
                    if area == True:
                        robo.bz.straight(-robo.bz.distance())
                    print('verificando area')

                elif robo.ultrassonicoFrente.distance() < 380 - robo.bz.distance():
                    print("capturar")
                    robo.bz.straight(distancia/2)
                    robot.capturar()
                    robo.bz.stop()
                    robo.bz.straight(distancia - robo.bz.distance())                    


                



    coordenada = None
    if ultima == False:
        #corrige a distânccia peercorrida
        if robo.bz.distance() > distancia and variavel ==  False:
            diferenca = robo.bz.distance() - distancia
            robo.bz.straight(-diferenca)


        coordenada = Coordenada(Coordenada(0 , y+1, explorada=True, comArea= area, saida= saida))



    return coordenada