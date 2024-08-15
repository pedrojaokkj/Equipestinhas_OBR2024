#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo


def captura():
    print('Wild VÍTIMA appearead!')


    robo.garra.run(-400)
    print("Bizzoru used POKE BALL!")
    robo.wait(2000)
    robo.bz.stop()

    robo.garra.run(400)
    print("Gotcha!")
    robo.wait(2000)
    robo.bz.stop()
