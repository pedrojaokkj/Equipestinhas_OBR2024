#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo
from ...Coordenada.coordenada import Coordenada
from ...Direcao.direcao import Direcao


def criarLadrilhoY(self, x, y, area = False, exp = True, sai = True, ent = False):

    ladrilho = Coordenada(x, y, comArea= area, explorada=exp, saida= sai ,entrada= ent)

    return ladrilho