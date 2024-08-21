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
    y_atual = 2
    andouAteDireita = 0

    while True:
        
        coordenadaDireita, final = andarEscaneandoX(Direcao('direita'))
        if final == True:
            ultimaDireita = coordenadaDireita
            coordenadas.append(ultimaDireita)
            # add virar até esquerda
            if ultimaDireita.saida != (True, Direcao('direita')):
                print('Se alinhar na parede')
                #implementar
            break
        
        andouAteDireita += 1


    while True:
        
        coordenada, final = andarEscaneandoX(Direcao('esquerda'))

        if final == True:
            robot.virarAte(Direcao('direita'))
            if coordenada.saida != (True, Direcao('esquerda')):
                print('Se alinhar na parede')
                #implementar
            break 

        coordenadas.append(coordenada)
    


        



    return andouAteDireita, coordenadas, mapa