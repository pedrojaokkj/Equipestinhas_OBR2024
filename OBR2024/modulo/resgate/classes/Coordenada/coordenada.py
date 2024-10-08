#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo 
from ..Direcao.direcao import Direcao



class Coordenada:


    def __init__(self, x:int = 0, y:int  = 0, comArea : bool = False, explorada : bool = False, saida : list[bool, Direcao] = [False, None], entrada = False) -> None:
        '''Cria uma Instancia do objeto

        Parameters:
            x(int) : Linha onde o robô se encontra
            y(int) : Coluna onde o robô se encontra
        '''



        self._x = x
        self._y = y
        self._posicao = (x, y)
        self._comArea = comArea
        self._explorada = explorada
        self._saida = saida
        self._entrada = entrada







    # Getters e Setters para _x
    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, valor: int) -> None:
        if isinstance(valor, int) and valor in [0,1,2,3,4] :
            self._x = valor
            self._posicao = (valor, self._y)  # Atualiza _posicao
        else:
            raise ValueError("O valor de x deve ser um número entre 1 e 4.")

    # Getters e Setters para _y
    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, valor: int) -> None:
        if isinstance(valor, int) and valor in [0,1,2,3,4] :
            self._y = valor
            self._posicao = (self._x, valor)  # Atualiza _posicao
        else:
            raise ValueError("O valor de y deve ser um número entre 1 e 4.")

    # Getter para _posicao
    @property
    def posicao(self) -> tuple[int, int]:
        return self._posicao

    # Getters e Setters para _comArea
    @property
    def comArea(self) -> bool:
        return self._comArea

    @comArea.setter
    def comArea(self, valor: bool) -> None:
        if isinstance(valor, bool) and 2 not in [self._x, self._y] and True not in [self._comArea, self._saida[0], self._entrada]:
            self._comArea = valor
        else:
            raise ValueError("O valor de comArea deve ser um booleano.")

    # Getters e Setters para _explorada
    @property
    def explorada(self) -> bool:
        return self._explorada

    @explorada.setter
    def explorada(self, valor: bool) -> None:
        if isinstance(valor, bool):
            self._explorada = valor
        else:
            raise ValueError("O valor de explorada deve ser um booleano.")

    # Getters e Setters para _saida
    @property
    def saida(self) -> list[bool, Direcao]:
        return self._saida

    @saida.setter
    def saida(self, valor: list[bool, Direcao]) -> None:
        if isinstance(valor, list[bool, Direcao]) and True not in [self._comArea, self._saida[0]]:
            self._saida = valor
        else:
            raise ValueError("O valor de saida deve ser um booleano.")

    # Getters e Setters para _entrada
    @property
    def entrada(self) -> bool:
        return self._entrada

    @entrada.setter
    def entrada(self, valor: bool) -> None:
        if isinstance(valor, bool) and True not in [self._comArea, self._entrada]:
            self._entrada = valor
        else:
            raise ValueError("O valor de entrada deve ser um booleano.")

        





    def exibir_propriedades(self) -> None:

        print('')
        print("Posição: ({}, {})".format(self.x, self.y))
        print("Com Área: {}".format(self.comArea))
        print("Explorada: {}".format(self.explorada))
        print("Saída: {}".format(self.saida))
        print("Entrada: {}".format(self.entrada))
        print('')