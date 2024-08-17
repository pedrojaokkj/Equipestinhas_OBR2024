#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo

class Parede:
    

    def __init__(self, valor:str) -> None:
        '''Cria uma Instancia do objeto

        Parameters:
            valor(str) : Valor em string que representa a parede('a', 'b', 'c', 'd')
        '''


        if not isinstance(valor, str) or valor.casefold() in ['a', 'b', 'c', 'd'] == False:
            raise ValueError("Valor deve ser uma string 'a', 'b', 'c', 'd'")
        self._valor = valor.casefold()




    @property
    def valor(self):
        return self._valor




    @valor.setter
    def valor(self, valor):
        if not isinstance(valor, str) or valor.casefold() in ['a', 'b', 'c', 'd'] :
            raise ValueError("Valor deve ser uma string 'a', 'b', 'c', 'd'"== False)
        self._valor = valor.casefold()

