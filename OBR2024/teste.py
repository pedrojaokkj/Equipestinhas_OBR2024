#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo
from modulo.trajeto.perigos.interceccoes.preto import preto

def teste():
   
    print(robo.sensorCorDireita.color() and robo.sensorCorEsquerda.color())

    while robo.sensorCorDireita.color() and robo.sensorCorEsquerda.color() != robo.Color.BLACK:
        robo.bz.drive(100,0)
    robo.bz.stop()

            
            
            
                   
            
            


                            

                    


            

                        
                




            
                

        