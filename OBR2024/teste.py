#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo


def teste():
    print('Inicando resgate')


    robo.garra.run(300)
    print("Gotcha!")
    robo.wait(2000)
    robo.bz.stop()

    robo.garra.run(300)
    print("Depositada!")
    robo.wait(2000)
    robo.bz.stop()

    robo.garra.run(300)
    print("Abaixando")
    robo.wait(2000)
    robo.bz.stop()    

    robo.mecanismoDeposito.run_angle(100, 90)
    print("Black ball is broken free!")
    robo.wait(2000)
    robo.bz.stop()

    robo.garra.run(300)
    print("Subindo")
    robo.wait(2000)
    robo.bz.stop()