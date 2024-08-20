#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo
from ...Mapa.mapa import Mapa
from ...Coordenada.coordenada import Coordenada



def escanearFrenteY(self, mapa):
    coordenadas : list[Coordenada] = []
    final = False
    y_atual = 1
    paredes_esquerda = []
    while final == False:
        if y_atual == 4:
            # checa saida
            mapa.adcionarY()
            final = True




    # vira até : trás
    # anda dois ladrilhos
    return coordenadas, mapa


def escanearFrenteX(self, mapa):
    coordenadas : list[Coordenada] = []
    final = False
    y_atual = 2
    andouAteDireita = 0
    while final == False:
        if y_atual == 4:
            # checa saida
            mapa.adcionarY()
            final = True




    # vira até : trás
    # anda dois ladrilhos
    #  vira até : esquerda
    return andouAteDireita, coordenadas, mapa