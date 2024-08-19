#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo


def captura():
    bz = robo.bz
    bz.settings(200)

    robo.garra.run_time(-1000,2000)
    bz.straight(30)
    bz.straight(-30)
    robo.garra.run_time(800,500)
    robo.garra.run_time(-1000,500)

    robo.garra.run_time(250,2000)
    robo.wait(1000)
    robo.garra.run_angle(-1000,65)
    robo.garra.run_time(1000,2000)

