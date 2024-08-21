#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo
from modulo.trajeto.perigos.interceccoes.preto import preto
from modulo.trajeto.perigos.interceccoes.pretoOuVerde import pretoOuVerde
from modulo.trajeto.perigos.interceccoes.becoOuDoisPretos import becoOuDoisPretos
from modulo.trajeto.checagens.confirmaCor import confirmaCor
from modulo.trajeto.checagens.alinhar import alinhar
from modulo.resgate.classes.Sala.funcoesConstrutoras.verificarPadroes import verificar_padroes

def teste():
    leituras = []
    while robo.ultrassonicoFrente.distance() > 50:

        robo.bz.drive(60, 0)
        leituras.append(robo.ultrassonicoFrente.distance())
        decrescente, variavel = verificar_padroes(leituras, 10)

        if variavel and len(leituras) > 30:
            print("leitura incoerente")
            break
            
    robo.bz.stop()


            
            
                   
            
            


                            

                    


            

                        
                







