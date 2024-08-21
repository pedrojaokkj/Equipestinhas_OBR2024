#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo
from ...Coordenada.coordenada import Coordenada
from ...Direcao.direcao import Direcao
from .verificarPadroes import verificar_padroes


def andarEscaneandoX(direcao : Direcao):

    saida = (False, None)
    robo.bz.reset()
    parede = False

    # add função de captura

    distancia =  0 #atribuir
    
    if robo.ultrassonicoFrente.distance() < 65:
        #checar parede
        print('Checando parede...')

    if parede == False:
        while robo.bz.distance < distancia:
            robo.bz.drive(60)
            if robo.sensorCorDireita.reflection() < 17:
                print('Saida encontrada')
                saida = (True, direcao)
                
                percorrido = robo.bz.distance()
                robo.bz.straight(-percorrido)
                break

            if robo.bz.distance() == distancia/2:
                print('Metade do trajeto, checando vitimas...')
                #add pegar vitimas

    return Coordenada(y = 2, explorada=True, saida= saida), parede
