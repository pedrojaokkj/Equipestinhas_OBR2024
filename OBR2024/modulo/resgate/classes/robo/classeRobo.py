#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________

from ..Direcao.direcao import Direcao
from ..Coordenada.coordenada import Coordenada
from .metodos import RoboGettersSetters


class Robo(RoboGettersSetters):
    def __init__(self,
                 altura: float = 250, 
                 largura: float = 200,
                 comprimento: float = 210,
                 direcaoAtual: Direcao = Direcao('frente'),
                 coordenadaAtual: Coordenada = Coordenada(0, 1)
                 ) -> None:
        '''Classe para representar o robô com altura, largura, comprimento, direção atual e coordenada atual'''

        self._altura = altura
        self._largura = largura
        self._comprimento = comprimento
        self._direcaoAtual = direcaoAtual
        self._coordenadaAtual = coordenadaAtual

# O arquivo `robo.py` importa os getters e setters da classe `RoboGettersSetters`, 
