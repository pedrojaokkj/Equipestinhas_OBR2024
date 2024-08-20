#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ....robo import robo
from ...checagens.alinhar import alinhar

def doisPretos():
    print('Duplo preto')
    robo.bz.straight(65)
    alinhar()