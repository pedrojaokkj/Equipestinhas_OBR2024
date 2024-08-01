#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo
Color = robo.Color 

# Verifica se o robô está na entrada da sala
def entradaDaSala():
    '''Faz a soma de 3 números inteiros e devolve como resposta um inteiro.
    
    Parameters:
        num1 (int): primeiro número a ser somado
        num2 (int): segundo número a ser somado
        num3 (int): terceiro número a ser somado
    
    Returns:
        soma (int): o valor da soma dos 3 números dados como argumento
    '''

    retorno = False
    if robo.ultrassonicoFrente.distance() > 850 or (robo.sensorCorDireita.color() != Color.WHITE and robo.sensorCorEsquerda.color() != Color.WHITE):
        retorno = False
    elif (robo.sensorCorDireita.reflection() > 98 and robo.sensorCorEsquerda.reflection() > 98):
        retorno = True

    return retorno