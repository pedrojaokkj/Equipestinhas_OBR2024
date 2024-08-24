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
    if robo.ultrassonicoFrente.distance() > 1200 or robo.sensorCorDireita.color() != Color.WHITE and robo.sensorCorEsquerda.color() != Color.WHITE:
        retorno = False
    elif robo.sensorCorDireita.reflection() < 55 and robo.sensorCorEsquerda.reflection() < 55 and robo.sensorCorDireita.color() == Color.WHITE and robo.sensorCorEsquerda.color() == Color.WHITE:
        robo.bz.reset()
        cores = confirmaCor()
        
        vezesE, colorsE, percentualE = zip(*cores[2])
        vezesD, colorsD, percentualD = zip(*cores[3])
        if cores[0] == Color.WHITE and cores[1] == Color.WHITE:
            print('BRanco BRanco')
            if percentualE[colorsE.index(robo.Color.WHITE)] >= 98 and percentualD[colorsD.index(robo.Color.WHITE)] >= 98:
                print('Branco 100')
                print(robo.bz.distance())
                robo.bz.reset()
                while True:
                    if robo.sensorCorEsquerda.color() == Color.BLACK or robo.bz.angle() > 20: 
                        robo.bz.stop()
                        break    
                    robo.bz.drive(0,40)

                robo.bz.turn(-robo.bz.angle())
                preto = robo.sensorCorEsquerda.color() == Color.BLACK
                if preto == False:
                    retorno = True
                    print(robo.bz.distance())
                    robo.bz.reset()

                robo.bz.turn(-robo.bz.angle())
    
        print("Sala de resgate é {}".format(retorno))

    return retorno