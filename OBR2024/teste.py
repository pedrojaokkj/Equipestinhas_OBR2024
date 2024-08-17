#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo
from modulo.trajeto.perigos.interceccoes.preto import preto
from modulo.trajeto.perigos.interceccoes.pretoOuVerde import pretoOuVerde
from modulo.trajeto.perigos.interceccoes.becoOuDoisPretos import becoOuDoisPretos
from modulo.trajeto.checagens.confirmaCor import confirmaCor

def teste():
   
    print(robo.sensorCorDireita.color() and robo.sensorCorEsquerda.color())

    while robo.sensorCorDireita.color() and robo.sensorCorEsquerda.color() != robo.Color.BLACK:
        robo.bz.drive(100,0)
    robo.bz.stop()

            
            
            
                   
            
            


                            

                    


            

                        
                







