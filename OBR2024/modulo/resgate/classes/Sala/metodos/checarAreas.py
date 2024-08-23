#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo.classeRobo import Robo
from ...Coordenada.coordenada import Coordenada
from ...Mapa.mapa import Mapa
from ...Direcao.direcao import Direcao

from .depoistarArea import depositarArea


def checarAreas(self):
    ''' Adciona ao mapa da sala as areas de resgate.

    
    '''

    maxY = len(self._mapa.coordenadas[0]) - 1
    maxX = len(self._mapa.coordenadas) - 1



    while True:    
        quinas = [self._mapa.coordenadas[0][0], self._mapa.coordenadas[0][maxY], self._mapa.coordenadas[maxX][maxY], self._mapa.coordenadas[maxX][0]]
        areas = [quina for quina in quinas if quina.comArea == True]
        quinasInesploradas = [quina for quina in quinas if quina.explorada == False]

        if len(areas) == 2:

            break
        
        elif len(areas) == 1 and len(quinasInesploradas) == 1:
            coordenadaArea = quinasInesploradas[0]
            coordenadaArea.explorada =  True
            coordenadaArea.comArea = True 

            self._mapa.coordenadas[coordenadaArea.x - 1][coordenadaArea.y -1] = coordenadaArea

            self.depositarArea(areas[0])

    

        elif len(areas) == 0 and len(quinasInesploradas) == 2:
            for quina in quinasInesploradas:
                self._mapa.coordenadas[quina.x - 1][quina.y - 1].comArea = True
                self._mapa.coordenadas[quina.x - 1][quina.y - 1].explorada = True   

            self.depositarArea(self._mapa.coordenadas[quina.x - 1][quina.y - 1])                 

        else:
            for quina in quinasInesploradas:

                if quina == quinas[0]:
                    direcaoAlvo =  Direcao('tras')
                    coordenadaAlvo = self._mapa.coordenadas[1][1] 

                elif quina == quinas[1]:
                    direcaoAlvo =  Direcao('esquerda')
                    coordenadaAlvo = self._mapa.coordenadas[1][maxY - 1]

                elif quina  == quinas[2]:
                    direcaoAlvo =  Direcao('frente')
                    coordenadaAlvo = self._mapa.coordenadas[maxX - 1][maxY- 1]

                elif quina == quinas[3]:
                    direcaoAlvo =  Direcao('direita')
                    coordenadaAlvo = self._mapa.coordenadas[maxX - 1][1]

                self.enviarRobo(coordenadaAlvo, direcaoAlvo)


                area = True#chamar função de ler area

                if area == True:
                    self._mapa.coordenadas[quina.x - 1][quina.y -1].comArea = True
                    self._mapa.coordenadas[quina.x - 1][quina.y -1].explorada = True
                    break


                

        


        






    