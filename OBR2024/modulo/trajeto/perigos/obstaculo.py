#!/usr/bin/env pybricks-micropython

from ...robo import robo

# Desvia do obstáculo
def obstaculo():
    print("detectando o obstaculo")
    robo.bz.settings(100)

    while True:
        if robo.ultrassonicoFrente.distance() > 45:
           robo.bz.drive(100,0)
        else:
            robo.bz.straight(-20)
            robo.bz.turn(75)
            robo.bz.straight(-1000)
            print("dando a volta no obstaculo")
            while True:
                if robo.ultrassonicoLado.distance() < 2000:
                    robo.bz.drive(70,0)
                else:
                    robo.bz.straight(2000)
                    robo.bz.turn(-90)

                    while True:
                        if robo.ultrassonicoLado.distance() <= 150:
                             robo.bz.drive(70)
                        else:
                            robo.bz.straight(60)
                            robo.bz.turn(-90)

                            while robo.sensorCorEsquerda.color() != robo.Color.BLACK:
                                robo.bz.drive(80)
                                break
                            break
                        break


                        
                             
                        



