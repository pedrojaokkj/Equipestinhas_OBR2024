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

        bz.straight(-80)
        # se ajusta
        if robo.sensorCorDireita.reflection() > 98 and robo.sensorCorEsquerda.reflection() > 98:
                print("indo para x:1")
                bz.straight(190)



        







        
        









                
                
                        
        
        
      
        
        




    


            
            
            
                   
            
            


                            

                    


            

                        
                







