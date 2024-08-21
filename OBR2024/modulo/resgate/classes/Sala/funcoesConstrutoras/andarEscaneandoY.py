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
    distancia = 0 #adicionar distancia
    leituras = []
    saida = (False, Direcao(None))
    area = False
    ultima = False
    parede = False

    #add função capturar
    




    while robo.bz.distance() <  distancia:

        robo.bz.drive(60, 0)
        leituras.append(robo.ultrassonicoFrente.distance())
        decrescente, variavel = verificar_padroes(leituras)

        if y == 1 and robo.ultrassonicoFrente.distance() < 380 - robo.bz.distance() or y == 2 and leituras[0] > 380:

            print("capturar")
            robo.bz.straight(distancia/2)
            #add função capturar
            robo.bz.stop()
            robo.bz.straight(distancia - robo.bz.distance())
            


        elif y == 2 and len(leituras) > 25:
            
            if variavel:
                #verificar se area
                print('verificando area')

            else:
                print("capturar")
                #anda um bocado
                #add função capturar
                robo.bz.stop()
                robo.bz.straight(distancia - robo.bz.distance())


            

        elif y == 3:


            if parede == False:
                #checar
                print('checar parede')

            if parede == True:
                ultima = True

            elif len(leituras) > 25:

                if robo.sensorCorDireita.reflection() < 15:
                    saida = (True, Direcao('Frente'))
                    robo.bz.straight(-robo.bz.distance())
                    ultima = True

                elif variavel:

                    #verificar se area
                    print('verificando area')

                elif robo.ultrassonicoFrente.distance() < 380 - robo.bz.distance():
                    print("capturar")
                    #anda um bocado
                    #add função capturar
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