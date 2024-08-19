#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo
from modulo.trajeto.perigos.interceccoes.preto import preto
from modulo.trajeto.perigos.interceccoes.pretoOuVerde import pretoOuVerde
from modulo.trajeto.perigos.interceccoes.becoOuDoisPretos import becoOuDoisPretos
from modulo.trajeto.checagens.confirmaCor import confirmaCor

def teste():
    bz = robo.bz
    bz.settings(200)

    robo.garra.run_time(-1000,2000)
    bz.straight(30)
    bz.straight(-30)
    robo.garra.run_time(800,500)
    robo.garra.run_time(-1000,500)

    robo.garra.run_time(350,2000)
    robo.wait(1000)
    robo.garra.run_angle(-1000,65)
    robo.garra.run_time(1000,2000)

    


            
            
            
                   
            
            


                            

                    


            

                        
                







