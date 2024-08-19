#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo.robo import robo
from .metodos.getters_setter_coordenadas import x, y, posicao, comArea, explorada, saida, entrada

class Coordenada:


    def __init__(self, x:int, y:int, comArea : bool = False, explorada : bool = False, saida : bool = False, entrada = False) -> None:
        '''Cria uma Instancia do objeto

        Parameters:
            x(int) : Linha onde o robô se encontra
            y(int) : Coluna onde o robô se encontra
        '''

        if not isinstance(x, int) or x > 4 or x < 0 :
            raise ValueError("X deve ser um valor entre 1 e 4")
        

        if not isinstance(y, int) or y > 4 or y < 0 :
            raise ValueError("Y deve ser um valor entre 1 e 4")        



        self._x = x
        self._y = y
        self._posicao = (x, y)
        self._comArea = comArea
        self._explorada = explorada
        self._saida = saida
        self._entrada = entrada


    # Importando os getters e setters
    x = x
    y = y
    posicao = posicao
    comArea = comArea
    explorada = explorada
    saida = saida
    entrada = entrada

    





    