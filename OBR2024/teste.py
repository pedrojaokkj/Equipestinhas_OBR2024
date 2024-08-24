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
    
    while robo.ultrassonicoFrente.distance() > 40:
        robo.bz.drive(200,0)
    robo.bz.stop()
    
    print("detectando o obstaculo")
    robo.bz.turn(90)

    print('sensores detectam o preto da linha( antes do obstaculo)')        
    while robo.sensorCorEsquerda.color() != robo.Color.BLACK:
        robo.bz.drive(-100,0)
    robo.bz.stop()
    
    robo.bz.reset()
    print(robo.bz.distance())

    print('contornando obstaculo')
    while robo.ultrassonicoLado.distance() < 150:
        robo.bz.drive(100,0)
    robo.bz.stop()

    robo.bz.straight(160)
    distancia = robo.bz.distance()
    print(robo.bz.distance())

    robo.bz.turn(-90)

    while robo.ultrassonicoLado.distance() > 150:
            robo.bz.drive(100,0)
    robo.bz.stop()

    robo.wait(700)

    robo.bz.straight(20)

    while robo.ultrassonicoLado.distance() < 200:
        robo.bz.drive(100,0)
    robo.bz.stop()

    robo.wait(700)

    robo.bz.straight(200)
    robo.bz.turn(-85)

    robo.bz.reset()
    
    print('voltando para a linha(depois do obstaculo)')
    print('sensores detectam o preto da linha(depois do obstaculo)')
    while robo.bz.distance() < distancia - 70 and robo.sensorCorEsquerda.color() != robo.Color.BLACK and robo.sensorCorDireita.color() != robo.Color.BLACK: 
        robo.bz.drive(100,0)
    robo.bz.stop()

    robo.wait(700)

    print('robo se ajusta na linha')
    while robo.sensorCorEsquerda.color() and robo.sensorCorDireita.color() == robo.Color.BLACK:
        robo.bz.drive(100,0)
    robo.bz.stop()

    robo.bz.straight(40)
    robo.bz.turn(90)





    




            
            
                   
            
            


                            

                    


            

                        
                







