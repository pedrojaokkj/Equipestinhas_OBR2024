#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo

class Direcao:
    def __init__(self, valor:str) -> None:
        '''Cria uma Instancia do objeto

        Parameters:
            valor(str) : Direção para onde o robô aponta ou deve apontar('direita', 'esquerda', 'frente', 'tras' ou None)
        '''

        if valor is None:
            self._valor = None
        elif not isinstance(valor, str) or valor.lower() not in ['direita', 'esquerda', 'frente', 'tras']:
            raise ValueError("Valor deve ser uma string 'direita', 'esquerda', 'frente', 'tras' ou None")
        else:
            self._valor = valor.lower()



    @property
    def valor(self):
        return self._valor




    @valor.setter
    def valor(self, valor):
        if valor is None:
            self._valor = None
        elif not isinstance(valor, str) or valor.lower() not in ['direita', 'esquerda', 'frente', 'tras']:
            raise ValueError("Valor deve ser uma string 'direita', 'esquerda', 'frente', 'tras' ou None")
        else:
            self._valor = valor.lower()