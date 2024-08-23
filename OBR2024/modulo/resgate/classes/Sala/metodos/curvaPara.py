#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________

from ...Direcao.direcao import Direcao
from ...Coordenada.coordenada import Coordenada


def curvaPara(direcaoAtual : Direcao , coordenadaAtual : Coordenada, coordenadaAlvo : Coordenada):
    # Verifica se o X aumenta ou diminui
    if coordenadaAlvo.x > coordenadaAtual.x:
        direcaoNecessaria = Direcao('direita')
    elif coordenadaAlvo.x < coordenadaAtual.x:
        direcaoNecessaria = Direcao('esquerda')
    else:
        direcaoNecessaria = direcaoAtual  # não é necessário virar

    # Verifica se o Y aumenta ou diminui
    if coordenadaAlvo.y > coordenadaAtual.y:
        direcaoNecessaria = Direcao('frente')
    elif coordenadaAlvo.y < coordenadaAtual.y:
        direcaoNecessaria = Direcao('tras')

    # Verifica se a direção atual é igual à direção necessária
    return direcaoNecessaria


