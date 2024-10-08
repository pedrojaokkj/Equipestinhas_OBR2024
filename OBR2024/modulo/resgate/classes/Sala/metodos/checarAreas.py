#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo.classeRobo import Robo
from ...Coordenada.coordenada import Coordenada
from ...Mapa.mapa import Mapa
from ...Direcao.direcao import Direcao
from .irParaArea import irParaArea

from .depoistarArea import depositarArea


def checarAreas(self):
    ''' Adciona ao mapa da sala as areas de resgate.

    
    '''

    print('Conferindo areas..')


    maxY = len(self._mapa.coordenadas[0]) - 1
    maxX = len(self._mapa.coordenadas) - 1



    while True:    
        quinas = [self._mapa.coordenadas[0][0], self._mapa.coordenadas[0][maxY], self._mapa.coordenadas[maxX][maxY], self._mapa.coordenadas[maxX][0]]
        areas = [quina for quina in quinas if quina.comArea == True]
        quinasInexploradas = [quina for quina in quinas if quina.explorada == False]

        if len(areas) == 2:
            print('Leitura Completa')
            break
        
        elif len(areas) == 1 and len(quinasInexploradas) == 1:
            coordenadaArea = quinasInexploradas[0]
            coordenadaArea.explorada =  True
            coordenadaArea.comArea = True 

            self._mapa.coordenadas[coordenadaArea.x - 1][coordenadaArea.y -1] = coordenadaArea

            self.depositarArea(areas[0])

    

        elif len(areas) == 0 and len(quinasInexploradas) == 2:
            for quina in quinasInexploradas:
                self._mapa.coordenadas[quina.x - 1][quina.y - 1].comArea = True
                self._mapa.coordenadas[quina.x - 1][quina.y - 1].explorada = True   

            self.depositarArea(self._mapa.coordenadas[quina.x - 1][quina.y - 1])                 

        else:
            for quina in quinasInexploradas:

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


                area = irParaArea()

                print('Area : ', area)
                if area == True:
                    self._mapa.coordenadas[quina.x - 1][quina.y -1].comArea = True
                    self._mapa.coordenadas[quina.x - 1][quina.y -1].explorada = True
                    break


                
                

        


        






    