#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo
from ...robo.classeRobo import Robo
from ..funcoesConstrutoras.iniciarMapa import iniciarMapa
from ...Coordenada.coordenada import Coordenada
from ...Mapa.mapa import Mapa
from ...Direcao.direcao import Direcao

from ..metodos.curvaPara import curvaPara





def calcularDistancia(self, coordenadaFinal : Coordenada, direcaoFinal : Direcao, mapa : Mapa, cooredenadaAtual:Coordenada, direcaoAtual:Direcao, rota : list = []):
    diferencaY = coordenadaFinal.y - cooredenadaAtual.y
    diferencaX = coordenadaFinal.x - cooredenadaAtual.x 


    if diferencaX == 0 and diferencaY == 0 and direcaoAtual == direcaoFinal:
        rota = ['Cabou XD!']
        
    
    else:
        p1 = cooredenadaAtual
        p2 = cooredenadaAtual
        possibilidades = []
        
        if diferencaY != 0:
            p1 = mapa.coordenadas[cooredenadaAtual.x - 1][cooredenadaAtual.y - 1 + (diferencaY/abs(diferencaY))]
            if isinstance(p1, Coordenada): 
                possibilidades.append(p1)


        if diferencaX != 0:
            p2 = mapa.coordenadas[cooredenadaAtual.x - 1 + (diferencaY/abs(diferencaY))][cooredenadaAtual.y - 1]
            if isinstance(p2, Coordenada):
                possibilidades.append(p2)


        caminhos = []

        passo = 0
        for p in possibilidades:
            r = []
            curvaNecessaria = curvaPara(direcaoAtual, cooredenadaAtual, p)
            if curvaPara(direcaoAtual, cooredenadaAtual, p) == False:
                passo = 'seguir'
            else: 
                passo = curvaNecessaria

            caminhos.append(self.calcularDistancia(coordenadaFinal, direcaoFinal, mapa, p, curvaNecessaria))


        rota = min(caminhos, key=len)
        rota.insert(0, passo)

    return rota    
                    


def enviarRobo(self, coordenada : Coordenada, direcao : Direcao):
    mapa = self._mapa
    posicaoAtual = self._robo.coordenadaAtual
    direcaoAtual = self._robo.direcaoAtual

    
    mapaRestringido = Mapa(x = len(mapa.coordenadas), y = len(mapa.coordenadas[0]))

    def restricao(coordenada : Coordenada, mapa : Mapa):
        retorno = False
        maxY = len(mapa.coordenadas[0]) - 1
        maxX = len(mapa.coordenadas) - 1
        quinas = [mapa.coordenadas[0][0], mapa.coordenadas[0][maxY], mapa.coordenadas[maxX][maxY], mapa.coordenadas[maxX][0]]

        if coordenada.comArea == True:
            retorno = True
        elif coordenada in quinas and coordenada.explorada == False:
            retorno = True

        return retorno            

    
    mapaRestringido.coordenadas = [['Coordenada Restringida' if restricao(coordenada, mapa) else coordenada for coordenada in linha] for linha in mapa ]
    intruncoes = self.calcularDistancia(coordenada, direcao, mapaRestringido, posicaoAtual, direcaoAtual)

    for passo in intruncoes:
        if isinstance(passo, Direcao):
            self._robo.virarAte(passo)

        elif passo == 'seguir':
            self.andar_cordenada()
    
        else:
            print('Chegou')


