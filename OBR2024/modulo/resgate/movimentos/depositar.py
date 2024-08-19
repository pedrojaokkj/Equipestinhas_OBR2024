#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo

def deposito():


    robo.garra.run(-400)
    print("Abaixando")
    robo.wait(2000)
    robo.bz.stop()    

    robo.mecanismoDeposito.run(300)
    print("VÍTIMA was sent to Box1!")
    robo.wait(2000)
    robo.bz.stop()

    robo.mecanismoDeposito.run(-300)
    robo.wait(2000)
    robo.bz.stop()

    robo.garra.run(300)
    print("Subindo")
    robo.wait(2000)
    robo.bz.stop()