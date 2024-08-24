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

    quinas = [mapa.coordenadas[0][0], mapa.coordenadas[0][maxY], mapa.coordenadas[maxX][maxY], mapa.coordenadas[maxX][0]]


    while True:

        mapa = self._mapa
        maxY = len(mapa.coordenadas[0]) - 1
        maxX = len(mapa.coordenadas) - 1
        inexplorados = []

        for linha in mapa.coordenadas:
            for coordenada in linha:
                if coordenada.explorada == False and coordenada.x in (0, maxX) or coordenada.y  in (0, maxY):

                    inexplorados.append(coordenada)

        if len(inexplorados) == 0 or  self._saida[1] != None:

            break


        else:
            distancias = []
            for coordenada  in inexplorados:
                if coordenada.x == 0:
                    direcao = Direcao('esquerda')
                elif coordenada.x == maxX:
                    direcao =  Direcao('direita')
                elif coordenada.y == maxY:
                    direcao = Direcao('frente')
                elif coordenada.y == 0:
                    direcao = Direcao('tras')

                distancias.append(calcularDistancia(coordenada, direcao, mapa, self._robo.direcaoAtual, self._robo.coordenadaAtual))

            distancias.sort(key=len, reverse=True)

            executarInstrucoes(distancias[0])
            parede = self._robo.checarParedeouArea()

            if parede == False:
                coordenadaAtual = self._robo.coordenadaAtual 
                self._mapa.coordenadas[coordenadaAtual.x-1][coordenadaAtual.y-1].saida = (True, self._robo.direcaoAtual)
                self._saida = [coordenadaAtual,  self._robo.direcaoAtual]







            

        
        



        

    
    