#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from .....robo import robo


def checarParedeouArea():
    bz = robo.bz
    paredeouarea = False

    bz.stop()

    robo.garra.reset_angle(0)

    robo.garra.run_time(-150,700)
    robo.garra.stop()
    robo.wait(1400)
    print(robo.garra.angle())
    if robo.garra.angle() > -155:
        paredeouarea = True

    robo.garra.run_time(400,1000)

    print('Parede ou area : ',paredeouarea)

    return paredeouarea

        
    


    


    
