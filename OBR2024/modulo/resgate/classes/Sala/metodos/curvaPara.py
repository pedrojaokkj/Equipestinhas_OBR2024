#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________

from ...Direcao.direcao import Direcao
from ...Coordenada.coordenada import Coordenada


def curvaPara(direcaoAtual : Direcao , coordenadaAtual : Coordenada, coordenadaAlvo : Coordenada):
    curva = False

    if coordenadaAtual.y > coordenadaAlvo.y and direcaoAtual != Direcao('tras'):
        curva = Direcao('tras')

    elif coordenadaAtual.y < coordenadaAlvo.y and direcaoAtual != Direcao('frente'):
        curva = Direcao('frente')

    if coordenadaAtual.x < coordenadaAlvo.x and direcaoAtual != Direcao('direita'):
        curva = Direcao('direita')

    elif coordenadaAtual.x > coordenadaAlvo.x and direcaoAtual != Direcao('esquerda'):
        curva = Direcao('esquerda')
    
    return curva


