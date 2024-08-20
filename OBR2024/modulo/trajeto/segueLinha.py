#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ..robo import robo
from .perigos.interceccoes.preto import preto
from .perigos.interceccoes.verde import verde
from .perigos.interceccoes.becoOuDoisPretos import becoOuDoisPretos
from .perigos.interceccoes.pretoOuVerde import pretoOuVerde

sensorD = robo.sensorCorDireita
sensorE = robo.sensorCorEsquerda

Color = robo.Color

# Lógica de seguir linha
def segueLinha():
    '''Executa movimentos de acordo com a leitura dos sensores de cor.

    '''


    if sensorD.color() == Color.WHITE:     #se o sensor direito ler branco...



        if sensorE.color() == Color.WHITE:    # e o sensor esquerdo ler branco
            robo.bz.drive(120,0)

        elif sensorE.color() == Color.BLACK:   # e o sensor esquerdo ler preto
            pretoOuVerde(sensorE)

        elif sensorE.color() == Color.GREEN:    # e se o sensor esquerdo ler verde
            pretoOuVerde(sensorE)

        else:
            robo.bz.drive(40,0)            





    elif sensorD.color() == Color.BLACK:    #se o sensor direito ler preto...



        if sensorE.color() == Color.WHITE:    # e o sensor esquerdo ler branco
            pretoOuVerde(sensorD)

        elif sensorE.color() == Color.BLACK:   # e o sensor esquerdo ler preto
            becoOuDoisPretos()

        elif sensorE.color() == Color.GREEN:    # e se o sensor esquerdo ler verde
            becoOuDoisPretos()

        else:
            robo.bz.drive(40,0)            
    




    elif sensorD.color() == Color.GREEN:    #se o sensor direito ler verde...



        if sensorE.color() == Color.WHITE:    # e o sensor esquerdo ler branco
            pretoOuVerde(sensorD)

        elif sensorE.color() == Color.BLACK:   # e o sensor esquerdo ler preto
            becoOuDoisPretos()

        elif sensorE.color() == Color.GREEN:    # e se o sensor esquerdo ler verde
            becoOuDoisPretos()
    
        else:
            robo.bz.drive(40,0)
        


    else:
        robo.bz.drive(40,0)
