#!/usr/bin/env pybricks-micropython

from ...robo import robo

# Desvia do obstáculo
def obstaculo():
    print("Desviando...")
    robo.bz.settings(100)

    while True:
        if robo.ultrassonicoFrente.distance() > 45:
           robo.bz.drive(100)
        else:
            robo.bz.straight(-40)
            robo.bz.turn(90)
            robo.bz.straight(-50)

            while True:
                if robo.ultrassonicoLado.distance() <= 70:
                    robo.bz.drive(70)
                else:
                    robo.bz.straight(60)
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


                        
                             
                        



