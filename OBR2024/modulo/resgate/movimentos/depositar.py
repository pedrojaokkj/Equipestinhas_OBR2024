#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo

def depositar(AreaTrue = False):

    ''' Args(bool) : Com base no resultado de AreaTrue, 
    ele faz os movimentos para depositar as vítimas'''

    bz = robo.bz

    if AreaTrue == True:
        bz.straight(-310)

    else:
        bz.turn(180)

    robo.mecanismoDeposito.run_time(-1000,700)
    robo.garra.run_time(-1000,2000)
    robo.mecanismoDeposito.run_time(240,400)
    robo.mecanismoDeposito.run_time(-240,1000)
    robo.mecanismoDeposito.run_time(240,400)
    robo.mecanismoDeposito.run_time(-240,1000)
    robo.garra.run_time(1000,2000)







    