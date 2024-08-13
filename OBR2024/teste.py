#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo


def teste():
    print("testando obstaculo")
    while True:
        if robo.ultrassonicoFrente.distance() > 40:
           robo.bz.drive(100,0)
        else:
            robo.bz.straight(-20)
            robo.bz.stop()
            robo.motorEsquerdo.run_angle(240,360)
            robo.bz.straight(-90)

            print("dando a volta no obstaculo")
            while True: 
                if robo.ultrassonicoLado.distance() < 200:
                    robo.bz.drive(70,0)
                else:
                    robo.bz.straight(110)
                    robo.bz.stop()
                    robo.motorDireito.run_angle(240,360)
                    robo.bz.turn(-80)

                    while True:
                        if robo.ultrassonicoLado.distance() > 200:
                            robo.bz.drive(70,0)
                        else:
                            while True:
                                if robo.ultrassonicoLado.distance() < 200:
                                    robo.bz.drive(70,0)
                                else:
                                    robo.bz.straight(50)
                                    robo.bz.turn(-80)

                                    while robo.sensorCorEsquerda.color() != robo.Color.BLACK:
                                        robo.bz.drive(80)

                                    


                        
                




            
                

        