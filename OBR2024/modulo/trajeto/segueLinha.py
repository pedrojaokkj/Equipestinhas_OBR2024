#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ..robo import robo
from .perigos.interceccoes.preto import preto
from .perigos.interceccoes.verde import verde
from .perigos.interceccoes.becoOuDoisPretos import becoOuDoisPretos
from .perigos.interceccoes.pretoOuVerde import pretoOuVerde
from .checagens.alinhar import alinhar

sensorD = robo.sensorCorDireita
sensorE = robo.sensorCorEsquerda

Color = robo.Color
 
# Lógica de seguir linha
def segueLinha():
    '''Executa movimentos de acordo com a leitura dos sensores de cor.

    '''


    if sensorD.reflection() > 65:     #se o sensor direito ler branco...



        if sensorE.reflection() > 65:    # e o sensor esquerdo ler branco
            robo.bz.drive(120,0)

        else:   # e o sensor esquerdo ler preto
            pretoOuVerde(sensorE)

         

    else:    #se o sensor direito ler preto...



        if sensorE.reflection() > 65:    # e o sensor esquerdo ler branco
            pretoOuVerde(sensorD)

        else:   # e o sensor esquerdo ler preto
            becoOuDoisPretos()


        




