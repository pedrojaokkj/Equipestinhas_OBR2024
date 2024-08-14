#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo
from modulo.trajeto.perigos.interceccoes.preto import preto

def teste():
    print("testando obstaculo")
    print("identificando o obstaculo")
    while True:
        if robo.ultrassonicoFrente.distance() > 40:
           robo.bz.drive(100,0)
        else:
            
            while True:
                if robo.sensorCorEsquerda.color() != robo.Color.BLACK:
                    robo.bz.drive(-80,0)
                    print("dando a volta no obstaculo")

                    while True: 
                
                        if robo.ultrassonicoLado.distance() < 200:
                            robo.bz.drive(70,0)
                        else:
                            robo.bz.straight(140)
                            robo.bz.turn(-170)

                            while True: 
                                if robo.ultrassonicoLado.distance() > 100:
                                    robo.bz.drive(100,0)
                                else:
                            
                                    while True:
                                        if robo.ultrassonicoLado.distance() > 150:
                                            robo.bz.drive(80,0)
                                        else:
                                            robo.bz.straight(70)
                                            robo.bz.turn(-170)
                                            
                                            print("indo identificar a linha")
                                            while robo.sensorCorEsquerda.color() != robo.Color.BLACK:
                                                robo.bz.drive(80)

                                        

                                        break
                                    break
                                break
                            break
                        break
            
            
            
            
                   
            
            


                            

                    


            

                        
                




            
                

        