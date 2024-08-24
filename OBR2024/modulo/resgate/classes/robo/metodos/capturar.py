#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from .....robo import robo


def captura():
    bz = robo.bz
    bz.stop()

    robo.mecanismoDeposito.run_time(-1000,1000)
    robo.garra.run_time(-400, 2000)
    bz.straight(-40)
    bz.straight(40)

    robo.garra.run_time(1000,2000)

