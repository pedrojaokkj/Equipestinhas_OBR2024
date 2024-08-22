#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo


def alinhar():
    print('Alinhando...')

    robo.bz.reset()


    while robo.sensorCorEsquerda.reflection() > 65:
        robo.bz.drive(0, 40)
        if robo.bz.angle() > 18:
            break


    angulo1 = robo.bz.angle()
    robo.bz.stop()
    print('Angulo1 :', angulo1)
    robo.bz.turn(-angulo1)
    


    while robo.sensorCorDireita.reflection() > 65:
        robo.bz.drive(0, -40)
        if robo.bz.angle() < -18:
            break


    angulo2 = robo.bz.angle()
    robo.bz.stop()

    print('Angulo2 :', angulo2)
    robo.bz.turn( -angulo2)



    diferenca = angulo2 + angulo1

    print("diferenca : ", diferenca)
    if angulo1 == 0 and angulo2 == 0:
        print('Rampa')
        robo.bz.straight(65)
        alinhar()


    elif 0 in [angulo1, angulo2]:
        robo.bz.turn(-diferenca/2)
        robo.bz.straight(-15)
        robo.bz.turn(diferenca * 1)

    elif abs(diferenca) < 7:
        robo.bz.turn(diferenca)

    else:
        robo.bz.turn(-diferenca/2)
        robo.bz.straight(-10)
        robo.bz.turn(diferenca * 1)




    robo.bz.stop()
