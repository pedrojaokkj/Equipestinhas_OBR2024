#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo


def alinhar():

    robo.bz.reset()


    while robo.sensorCorEsquerda.reflection() > 65:
        robo.bz.drive(0, 40)

    angulo1 = robo.bz.angle()
    robo.bz.stop()
    print('Angulo1 :', angulo1)
    robo.bz.turn(-angulo1)
    
    print('Angulo1 :', robo.bz.angle())




    while robo.sensorCorDireita.reflection() > 65:
        robo.bz.drive(0, -40)

    angulo2 = robo.bz.angle()
    robo.bz.stop()

    print('Angulo2 :', angulo2)
    robo.bz.turn( -angulo2)

    print('Angulo1 :', robo.bz.angle())



    diferenca = angulo2 + angulo1

    print("diferenca : ", diferenca)

    if 0 in [angulo1, angulo2]:
        robo.bz.turn(-diferenca/2)
        robo.bz.straight(-diferenca)
        robo.bz.turn(diferenca * 1)

    elif abs(diferenca) < 7:
        robo.bz.turn(diferenca)

    else:
        robo.bz.turn(-diferenca/2)
        robo.bz.straight(-10)
        robo.bz.turn(diferenca * 1.2)


    robo.bz.stop()
