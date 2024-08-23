#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo
from ...robo.classeRobo import Robo
from ...Coordenada.coordenada import Coordenada
from ...Mapa.mapa import Mapa
from ...Direcao.direcao import Direcao
from .escanearFrenteY import escanearFrenteY
from .escanearFrenteX import escanearFrenteX
from .....trajeto.checagens.alinhar import alinhar


def iniciarMapa(self, robot : Robo, mapa : Mapa):
    ''' Faz as atribuções das propriedades no mapa da sala, centraliza o robô e retorna o mapa atualizado

    
    Returns:
        robot(Robo) : robo para a iniciação da classe Sala 
        mapa(Mapa) : Mapa da sala iniciada.
    '''

    saida = [Coordenada(x = 0, y=0), Direcao(None)]
    
    print("Alinhando...")
    robo.bz.straight(-40)
    alinhar()


    print("Entrando na sala...")
    print('Indo para y:1')
    robo.bz.straight(100)
    robot.capturar()
    robo.bz.straight(135)
    

    coordenadas_y_entrada, mapa = escanearFrenteY(robot, mapa)

    ateParedeDireita, coordenadas_x_y2, mapa = escanearFrenteX(robot, mapa)
    if len(coordenadas_x_y2) == 4:
        mapa.adcionarX()



    #quando chegar na parede x=1 y=2



    for i, coordenada in enumerate(coordenadas_x_y2):
        coordenada.x = len(coordenadas_x_y2) - i
        y = coordenada.y - 1
        x = coordenada.x - 1 

        mapa.coordenadas[x][y] = coordenada


     
    for coordenada in coordenadas_y_entrada:
        coordenada.x = len(coordenadas_x_y2) - ateParedeDireita 
        y = coordenada.y - 1
        x = coordenada.x - 1

        mapa.coordenadas[x][y] = coordenada


    print('"Here, this will help you."')
    print("ROBO received a Town Map from Daisy.")
    
    mapa.exibir_mapa()
    robot.direcaoAtual = Direcao('direita')
    robot.coordenadaAtual = mapa.coordenadas[1 - 1] [2 -1]

    #centralizar e finalizar


    #andarAté(x = 2, y = 2, direção, direita)
    print("Centralizando...")

    robo.bz.straight(270)
    robot.capturar()

    print("Centralizado x = 2 y = 2")

    robot.coordenadaAtual = mapa.coordenadas[1][1]


    self._saida = saida
    self._entrada = coordenadas_y_entrada[0]


    return (robot, mapa)