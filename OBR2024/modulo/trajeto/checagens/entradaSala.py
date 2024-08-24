#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo
from .confirmaCor import confirmaCor
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
    if robo.ultrassonicoFrente.distance() > 850 or robo.sensorCorDireita.color() != Color.WHITE and robo.sensorCorEsquerda.color() != Color.WHITE:
        retorno = False
    elif robo.sensorCorDireita.reflection() < 75 and robo.sensorCorEsquerda.reflection() < 75 and robo.sensorCorDireita.color() == Color.WHITE and robo.sensorCorEsquerda.color() == Color.WHITE:
        cores = confirmaCor()
        
        vezesE, colorsE, percentualE = zip(*cores[2])
        vezesD, colorsD, percentualD = zip(*cores[3])  
        if cores[0] == Color.WHITE and cores[1] == Color.WHITE:
            if percentualE[colorsE.index(robo.Color.WHITE)]> 99 and percentualD[colorsD.index(robo.Color.WHITE)]> 99:
                retorno = True
        print("Sala de resgate é {}".format(retorno))

    return retorno