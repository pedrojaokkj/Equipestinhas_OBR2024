#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ....robo import robo
from ..robo.classeRobo import Robo
from ..Coordenada.coordenada import Coordenada
from ..Mapa.mapa import Mapa
from ..Direcao.direcao import Direcao
from .funcoesConstrutoras.iniciarMapa import iniciarMapa
from .metodos.andar_cordenada import andar_cordenada
from .metodos.checarAreas import checarAreas
from .metodos.depoistarArea import depositarArea
from .metodos.sair import sair
from .metodos.explorar import explorar

from .metodos.enviarRobo import enviarRobo

class SalaDeResgate:

    def __init__(self, roboObj : Robo) -> None:
        '''Cria uma Instancia do objeto

        Parameters:
            robo(Robo): robo que entrou na sala de resgate
        '''
        
        self._entrada = [Coordenada(x = 0, y=1), Direcao('tras')]
        self._saida = [Coordenada(x = 0, y=0), Direcao(None)]
        self._robo, self._mapa = iniciarMapa(self, roboObj, Mapa())
        


    #atribuição das funções da classe

    def enviarRobo(self, coordenada : Coordenada, direcao : Direcao) -> None:
        '''Envia o robo para a coordenada desejada'''


        enviarRobo(self, coordenada, direcao)



    def andarCordenada(self):
        ''' Anda para a frente uma vez altera a posição do robo na classe.
        
        '''
        andar_cordenada(self)


    def depositarArea(self, coord):
        '''Deposita a em uma area na sala de resgate'''
        depositarArea(self, coord)



    def encontrarAreas(self):
        ''' Adciona ao mapa da sala as areas de resgate.

        
        '''
        checarAreas(self)


    def explorar(self):
        print('Esplorando ladrilhos restantes...')
        mapa = self._mapa
        inexplorados = []

        for linha in mapa.coordenadas:
            for coordenada in linha:
                if coordenada.explorada == False:
                    inexplorados.append(coordenada)


        


    def sair(self):
        
        mapa = self._mapa
        saida = [[coordenada for coordenada in linha if coordenada.saida[0] == True] for linha in mapa.coordenadas]

        if len(saida) == 1:
            saida = saida[0][0]

        else:
            self.explorar()
            mapa = self._mapa
            saida = [[coordenada for coordenada in linha if coordenada.saida[0] == True] for linha in mapa.coordenadas]

            if len(saida) == 1:
                saida = saida[0][0]
            else:
                return


        self.enviarRobo(saida, saida.saida[1])
                


        
                





    












        
    
