#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo
from modulo.trajeto.perigos.interceccoes.preto import preto
from modulo.trajeto.perigos.interceccoes.pretoOuVerde import pretoOuVerde
from modulo.trajeto.perigos.interceccoes.becoOuDoisPretos import becoOuDoisPretos
from modulo.trajeto.checagens.confirmaCor import confirmaCor
from modulo.resgate.movimentos.ladrilo_inicial import ladrilhoInicial
from modulo.resgate.movimentos.andar_cordenada import andar_cordenada


def teste():
    
    bz= robo.bz
    bz.settings(100)

    ladrilhoInicial()

    print('mudando de cordenada')

    bz.straight(300*2)




    




            
            
                   
            
            


                            

                    


            

                        
                







