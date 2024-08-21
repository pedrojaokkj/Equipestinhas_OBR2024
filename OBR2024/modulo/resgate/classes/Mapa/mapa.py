#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo
from ..robo.classeRobo import Robo 
from ..Coordenada.coordenada import Coordenada


class Mapa:
    def __init__(self, x : int = 3, y : int = 3) -> None:
        if not isinstance(x, int) or x > 4 or x < 3 :
            raise ValueError("X deve ser um valor entre 3 e 4")
        
        if not isinstance(y, int) or y > 4 or y < 3 :
            raise ValueError("Y deve ser um valor entre 3 e 4")
        
        if not isinstance(y, int) or x+y not in [6,7] :
            raise ValueError("A sala tem tamanho 3x3, 4x3, ou 3x4")   

        self.coordenadas = [[Coordenada(coluna + 1, linha + 1) for linha in range(y)] for coluna in range(x)]


    
    def exibir_mapa(self):
        for linha in self.coordenadas:
            print(' '.join(str((coord.x, coord.y)) for coord in linha))




    def adcionarX(self):
        if self.coordenadas.x == 4 or self.coordenadas.y == 3 :
            raise ValueError("A sala já tem o valor máximo")
        
        else:
            print('Adicionando Mais um x')
            self.coordenadas.append([Coordenada(4, i+1) for i in range(3)])




    def adcionarY(self):
        if self.coordenadas.x == 4 or self.coordenadas.y == 3 :
            raise ValueError("A sala já tem o valor máximo")
        
        else:
            for i in range(3):
                self.coordenadas[i].append(Coordenada(i+1, 4))
            print('Adicionando Mais um y')




