#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo
from ...Mapa.mapa import Mapa
from ...Coordenada.coordenada import Coordenada
from ...Direcao.direcao import Direcao
from ...robo.classeRobo import Robo

from .andarEscaneandoX import andarEscaneandoX

def escanearFrenteX(robot : Robo, mapa):
    coordenadas = []
    final = False
    andouAteDireita = 0

    while True:
        
        coordenadaDireita, final = andarEscaneandoX(robot, Direcao('direita'))
        if final == True:
            ultimaDireita = coordenadaDireita
            coordenadas.append(ultimaDireita)
            robot.virarAte(Direcao('esquerda'))
            if ultimaDireita.saida != (True, Direcao('direita')):
                print('Se alinhar na parede')
                robot.ajutarnaParede()
            break
        
        andouAteDireita += 1


    while True:
        
        coordenada, final = andarEscaneandoX(robot, Direcao('esquerda'))
        coordenada.exibir_propriedades()
        if final == True:
            robot.virarAte(Direcao('direita'))
            if coordenada.saida != (True, Direcao('esquerda')):
                print('Se alinhar na parede')
                robot.ajutarnaParede()
            break 

        coordenadas.append(coordenada)
    


        



    return andouAteDireita, coordenadas, mapa