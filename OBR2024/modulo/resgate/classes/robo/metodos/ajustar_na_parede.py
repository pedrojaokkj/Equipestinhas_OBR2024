#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from .....robo import robo

def ajutarnaParede():
    bz = robo.bz

    print('Se ajustando na parede')
    bz.straight(-120)

    print('Voltando para o meio do ladrilho')
    bz.straight(80)



