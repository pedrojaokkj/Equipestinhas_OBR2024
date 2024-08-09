#!/usr/bin/env pybricks-micropython

from ...robo import robo

# Desvia do obstáculo
def obstaculo():
    print("detectando o obstaculo")
    robo.bz.settings(100)

    while True:
        if robo.ultrassonicoFrente.distance() > 40:
           robo.bz.drive(100,0)
        else:
            robo.bz.straight(-20)
            robo.bz.turn(80)
            robo.bz.straight(-90)

            print("dando a volta no obstaculo")
            while True: 
                if robo.ultrassonicoLado.distance() < 300:
                    robo.bz.drive(100,0)
                else:
                    robo.bz.straight(165)
                    robo.bz.turn(-80)
                    robo.bz.straight(135)

                    while True:
                        if robo.ultrassonicoLado.distance() < 150:
                            robo.bz.drive(100,0)
                        else:
                            robo.bz.straight(200)
                            robo.bz.turn(-80)

                            while robo.sensorCorEsquerda.color() != robo.Color.BLACK:
                                robo.bz.drive(80)
                                break
                            break
                        break


                        
                             
                        



