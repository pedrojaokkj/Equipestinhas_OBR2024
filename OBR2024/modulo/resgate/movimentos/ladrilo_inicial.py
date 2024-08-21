#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo
from modulo.trajeto.checagens.alinhar import alinhar
''' Adicionar ladrilho_inicial em iniarMapa(line 27)'''

def ladrilhoInicial():
    bz= robo.bz
    bz.settings(100)

    print('Indo para trás e se alinhando na linha do trajeto')
    bz.straight(-40)
    alinhar()
    

    print('Indo para y:1')
    bz.straight(235)


