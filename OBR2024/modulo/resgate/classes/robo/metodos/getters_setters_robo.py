#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________

from ...Direcao.direcao import Direcao
from ...Coordenada.coordenada import Coordenada

class RoboGettersSetters:
    # Getters e Setters para os atributos

    # Altura
    @property
    def altura(self) -> float:
        return self._altura
    
    @altura.setter
    def altura(self, value: float) -> None:
        if value > 0:
            self._altura = value
        else:
            raise ValueError("Altura deve ser um valor positivo")

    # Largura
    @property
    def largura(self) -> float:
        return self._largura
    
    @largura.setter
    def largura(self, value: float) -> None:
        if value > 0:
            self._largura = value
        else:
            raise ValueError("Largura deve ser um valor positivo")

    # Comprimento
    @property
    def comprimento(self) -> float:
        return self._comprimento
    
    @comprimento.setter
    def comprimento(self, value: float) -> None:
        if value > 0:
            self._comprimento = value
        else:
            raise ValueError("Comprimento deve ser um valor positivo")

    # Direção Atual
    @property
    def direcaoAtual(self) -> Direcao:
        return self._direcaoAtual
    
    @direcaoAtual.setter
    def direcaoAtual(self, value: Direcao) -> None:
        self._direcaoAtual = value

    # Coordenada Atual
    @property
    def coordenadaAtual(self) -> Coordenada:
        return self._coordenadaAtual
    
    @coordenadaAtual.setter
    def coordenadaAtual(self, value: Coordenada) -> None:
        self._coordenadaAtual = value

















class RoboGettersSetters:
    # Getters e Setters para os atributos

    # Altura
    @property
    def altura(self) -> float:
        return self._altura
    
    @altura.setter
    def altura(self, value: float) -> None:
        if value > 0:
            self._altura = value
        else:
            raise ValueError("Altura deve ser um valor positivo")

    # Largura
    @property
    def largura(self) -> float:
        return self._largura
    
    @largura.setter
    def largura(self, value: float) -> None:
        if value > 0:
            self._largura = value
        else:
            raise ValueError("Largura deve ser um valor positivo")

    # Comprimento
    @property
    def comprimento(self) -> float:
        return self._comprimento
    
    @comprimento.setter
    def comprimento(self, value: float) -> None:
        if value > 0:
            self._comprimento = value
        else:
            raise ValueError("Comprimento deve ser um valor positivo")

    # Direção Atual
    @property
    def direcaoAtual(self) -> Direcao:
        return self._direcaoAtual
    
    @direcaoAtual.setter
    def direcaoAtual(self, value: Direcao) -> None:
        self._direcaoAtual = value

    # Coordenada Atual
    @property
    def coordenadaAtual(self) -> Coordenada:
        return self._coordenadaAtual
    
    @coordenadaAtual.setter
    def coordenadaAtual(self, value: Coordenada) -> None:
        self._coordenadaAtual = value
