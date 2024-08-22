#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________


from .....robo import robo
from ...Direcao.direcao import Direcao
from ...Coordenada.coordenada import Coordenada

def virar(self, direcaoAlvo : Direcao):
    '''Vira o Robô para a direção desejada pelo caminho mais próximo
    
    '''


    direcoes = {'frente' : (0, 4, 8), 'direita' : (1, 5, 9), 'tras' : (2, 6, 10), 'esquerda' : (3, 7, 11)}


    direcaoAtual = self.direcaoAtual.valor
    valorAlvo = direcaoAlvo.valor

    print('Direção atual :', direcaoAtual)
    print('Direção alvo :', direcaoAlvo)

    indiceAtual = direcoes[direcaoAtual][1]

    if indiceAtual > direcoes[valorAlvo][1]:

        indiceAlvoAH = direcoes[valorAlvo][1]
        indiceAlvoH = direcoes[valorAlvo][2]

    else:
        indiceAlvoAH = direcoes[valorAlvo][0]
        indiceAlvoH = direcoes[valorAlvo][1]


    distanciaHorario =  indiceAlvoH - indiceAtual
    distanciaAntiHorario = indiceAtual - indiceAlvoAH

    if distanciaAntiHorario == distanciaHorario:
        #gire 180 graus
        print('Girando 180 graus')
        robo.bz.turn(180)

    elif distanciaAntiHorario < distanciaHorario:
        #gire no sentido antiHorario
        print('Girando até : {} Sentido Anti-Horário'.format(valorAlvo))
        robo.bz.turn(-90)

    else:
        #gire no sentido horario
        print('Girando até : {} Sentido Horário'.format(valorAlvo))
        robo.bz.turn(90)
 
    self.direcaoAtual = direcaoAlvo

