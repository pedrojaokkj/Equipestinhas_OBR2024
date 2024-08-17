#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo.robo import robo

class Coordenada:



    def __init__(self, x:int = 0, y:int = 0) -> None:
        '''Cria uma Instancia do objeto

        Parameters:
            x(int) : Linha onde o robô se encontra
            y(int) : Coluna onde o robô se encontra
        '''



        self._x = x
        self._y = y
        self._posicao = (x, y)



    @property
    def x(self):
        return self._x



    @x.setter
    def x(self, valor):
        if not isinstance(valor, int) or valor > 4 or valor < 1 :
            raise ValueError("X deve ser um valor entre 1 e 4")
        self._x = valor



    @property
    def y(self):
        return self._y




    @y.setter
    def y(self, valor):
        if not isinstance(valor, int) or valor > 4 or valor < 1 :
            raise ValueError("Y deve ser um valor entre 1 e 4")
        self._y = valor



    @property
    def posicao(self):
        return self._posicao



    @posicao.setter
    def nome(self, valor):
        if not isinstance(valor, tuple) or valor[0] > 4 or valor[0] < 1 or valor[1] > 4 or valor[1] < 1 :
            raise ValueError("Posicao deve ser uma tupla de dois valores entre 1 e 4")
        self._posicao = valor

    

