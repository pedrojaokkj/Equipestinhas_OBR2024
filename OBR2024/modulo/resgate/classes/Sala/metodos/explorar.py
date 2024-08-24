#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo.classeRobo import Robo
from ...Coordenada.coordenada import Coordenada
from ...Mapa.mapa import Mapa
from ...Direcao.direcao import Direcao

from .enviarRobo import calcularDistancia, executarInstrucoes


def explorar(self):
    ''' Vai até os ladrilhos inexplorado, procurando pela saida e pelas vitimas
    
    
    '''



    print('Esplorando ladrilhos restantes...')

    while True:

        mapa = self._mapa
        maxY = len(mapa.coordenadas[0]) - 1
        maxX = len(mapa.coordenadas) - 1
        inexplorados = []

        for linha in mapa.coordenadas:
            for coordenada in linha:
                if coordenada.explorada == False and coordenada.x == maxX or coordenada.y  == maxY:

                    inexplorados.append(coordenada)

        if len(inexplorados) == 0 or  self._saida[1] != None:

            break


        # else:
        #     calcularDistancia()

        
        



        

    
    