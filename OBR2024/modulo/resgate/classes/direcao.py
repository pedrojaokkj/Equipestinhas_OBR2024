#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo

class Direcao:
    def __init__(self, valor:str) -> None:
        '''Cria uma Instancia do objeto

        Parameters:
            valor(str) : Direção para onde o robô aponta ou deve apontar('direita', 'esquerda', 'cima', 'baixo')
        '''

        if not isinstance(valor, str) or valor.casefold() in ['direita', 'esquerda', 'cima', 'baixo'] == False:
            raise ValueError("Valor deve ser uma string 'direita', 'esquerda', 'cima', 'baixo'")
        self._valor = valor.casefold()



    @property
    def valor(self):
        return self._valor




    @valor.setter
    def valor(self, valor):
        if not isinstance(valor, str) or valor.casefold() in ['direita', 'esquerda', 'cima', 'baixo'] :
            raise ValueError("Valor deve ser uma string 'direita', 'esquerda', 'cima', 'baixo'"== False)
        self._valor = valor.casefold()