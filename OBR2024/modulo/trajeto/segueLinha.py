#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ..robo import robo
from .perigos.interceccoes.preto import preto
from .perigos.interceccoes.verde import verde
from .perigos.interceccoes.becoOuDoisPretos import becoOuDoisPretos

sensorD = robo.sensorCorDireita
sensorE = robo.sensorCorEsquerda

Color = robo.Color

# Lógica de seguir linha
def segueLinha():
    '''Executa movimentos de acordo com a leitura dos sensores de cor.

    '''


    if sensorD.color() == Color.WHITE:     #se o sensor direito ler branco...



        if sensorE.color() == Color.WHITE:    # e o sensor esquerdo ler branco
            robo.bz.drive(200,0)

        elif sensorE.color() == Color.BLACK:   # e o sensor esquerdo ler preto
            preto(sensorE)

        elif sensorE.color() == Color.GREEN:    # e se o sensor esquerdo ler verde
            verde(sensorE)





    elif sensorD.color() == Color.BLACK:    #se o sensor direito ler preto...



        if sensorE.color() == Color.WHITE:    # e o sensor esquerdo ler branco
            preto(sensorD)

        elif sensorE.color() == Color.BLACK:   # e o sensor esquerdo ler preto
            becoOuDoisPretos()

        elif sensorE.color() == Color.GREEN:    # e se o sensor esquerdo ler verde
            becoOuDoisPretos()
    




    elif sensorD.color() == Color.GREEN:    #se o sensor direito ler verde...



        if sensorE.color() == Color.WHITE:    # e o sensor esquerdo ler branco
            verde(sensorD)

        elif sensorE.color() == Color.BLACK:   # e o sensor esquerdo ler preto
            becoOuDoisPretos()

        elif sensorE.color() == Color.GREEN:    # e se o sensor esquerdo ler verde
            becoOuDoisPretos()