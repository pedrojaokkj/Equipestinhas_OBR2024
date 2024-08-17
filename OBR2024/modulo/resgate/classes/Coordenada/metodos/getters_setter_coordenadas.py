#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from coordenada import Coordenada




# Getters e Setters para _x
@property
def x(self) -> int:
    return self._x

@x.setter
def x(self, valor: int) -> None:
    if isinstance(valor, int):
        self._x = valor
        self._posicao = (valor, self._y)  # Atualiza _posicao
    else:
        raise ValueError("O valor de x deve ser um inteiro.")

# Getters e Setters para _y
@property
def y(self) -> int:
    return self._y

@y.setter
def y(self, valor: int) -> None:
    if isinstance(valor, int):
        self._y = valor
        self._posicao = (self._x, valor)  # Atualiza _posicao
    else:
        raise ValueError("O valor de y deve ser um inteiro.")

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
    if isinstance(valor, bool):
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
def saida(self) -> bool:
    return self._saida

@saida.setter
def saida(self, valor: bool) -> None:
    if isinstance(valor, bool):
        self._saida = valor
    else:
        raise ValueError("O valor de saida deve ser um booleano.")

# Getters e Setters para _entrada
@property
def entrada(self) -> bool:
    return self._entrada

@entrada.setter
def entrada(self, valor: bool) -> None:
    if isinstance(valor, bool):
        self._entrada = valor
    else:
        raise ValueError("O valor de entrada deve ser um booleano.")