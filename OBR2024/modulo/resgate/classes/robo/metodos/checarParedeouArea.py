#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from .....robo import robo


def checarParedeouArea():
    bz = robo.bz
    paredeouarea = False

    bz.reset()
    print(robo.garra.angle())
    robo.garra.run_time(-150,700)
    robo.garra.stop()
    robo.wait(1400)
    print(robo.garra.angle())
    if robo.garra.angle() > -140:
        paredeouarea = True

    return paredeouarea

        
    


    


    
