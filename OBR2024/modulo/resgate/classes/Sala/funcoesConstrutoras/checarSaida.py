#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo


def checarSaida():
    ''' Verifica se tem uma abertura na frente do robô

    Returns:
        saida(bool) : True se houver saída e false se não houver
    
    '''
    
    if robo.ultrassonicoFrente.distance() > 100:
        saida = True
    else:
        leituraUltrassonico = robo.ultrassonicoFrente.distance()
        robo.bz.reset()
        #capturar
        robo.bz.straight(-robo.bz.distance())
        if robo.ultrassonicoFrente.distance() > leituraUltrassonico + 10:
            saida = True
        else:
            saida = False

    return saida