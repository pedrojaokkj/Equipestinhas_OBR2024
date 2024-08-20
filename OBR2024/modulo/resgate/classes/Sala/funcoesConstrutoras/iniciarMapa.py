#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo
from ...robo.classeRobo import Robo
from ...Coordenada.coordenada import Coordenada
from ...Mapa.mapa import Mapa
from ...Direcao.direcao import Direcao
from .escanearFrente import escanearFrenteY, escanearFrenteX


def iniciarMapa(self, mapa : Mapa):
    ''' Faz as atribuções das propriedades no mapa da sala, centraliza o robô e retorna o mapa atualizado

    
    Returns:
        mapa(Mapa) : Mapa da sala iniciada.
    '''

    saida = list[Coordenada, Direcao] = [Coordenada(x = 0, y=0), Direcao(None)]
    
    print("Alinhando...")
    #alinhar

    print("Entrando na sala...")
    #ir até ladrilho inicial
    x_atual : int = 0
    y_atual : int = 1

    coordenadas_y_entrada, mapa = escanearFrenteY(self, mapa)
    ateParedeDireita, coordenadas_x_y2, mapa = escanearFrenteX(self, mapa)



    #quando chegar na parede x=1 y=2

    if coordenadas_x_y2 == 4:
        mapa.adcionarX()


    for i, coordenada in enumerate(coordenadas_x_y2):
        coordenada.x = len(coordenadas_x_y2) - i
        y = coordenada.y() - 1
        x = coordenada.x() - 1 

        mapa.coordenadas[x][y] = coordenada



    for coordenada in coordenadas_y_entrada:
        coordenada.x = len(coordenadas_x_y2) - ateParedeDireita 
        y = coordenada.y() - 1
        x = coordenada.x() - 1

        mapa.coordenadas[x][y] = coordenada


    #centralizar e finalizar

    self._robo.coordenadaAtual(Coordenada(2, 2, explorada=True))
    self._robo.direcaoAtual(Direcao('direta'))
    self._saida = saida
    self._entrada = coordenadas_y_entrada[1]


    return (mapa)