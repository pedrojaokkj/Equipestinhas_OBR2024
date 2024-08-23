#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo
from modulo.trajeto.perigos.interceccoes.preto import preto
from modulo.trajeto.perigos.interceccoes.pretoOuVerde import pretoOuVerde
from modulo.trajeto.perigos.interceccoes.becoOuDoisPretos import becoOuDoisPretos
from modulo.trajeto.checagens.confirmaCor import confirmaCor
from modulo.resgate.movimentos.ladrilo_inicial import ladrilhoInicial
from modulo.resgate.classes.Sala.metodos.andar_cordenada import andar_cordenada
from modulo.resgate.classes.robo.metodos.checarParedeouArea import checarParedeouArea
from modulo.resgate.classes.robo.metodos.capturar import captura
from modulo.resgate.movimentos.depositar import depositar


def teste():
    
    bz = robo.bz
    bz.reset()
    bz.turn(45)
    bz.reset()
    
    bz.straight(80)
    captura()

    while robo.ultrassonicoFrente.distance() > 65:
        bz.drive(100,0)
    bz.stop()
    
    distancia = robo.bz.distance()
    
    area = checarParedeouArea()

    if area == True:
            bz.turn(180)
            depositar(True)
            bz.straight(50)
            bz.turn(180)
            bz.straight(100)

    while robo.ultrassonicoFrente.distance() < 65:
        bz.drive(100,0)
    bz.stop()

    bz.straight(-distancia)
    bz.turn(-45)

    return area




    


    
         
        
    return
        
    




    









    




            
            
                   
            
            


                            

                    


            

                        
                







