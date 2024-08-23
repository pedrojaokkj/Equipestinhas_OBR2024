#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ....robo import robo
from modulo.trajeto.checagens.alinhar import alinhar

def becoSemSaida():
    '''Faz o robô dar meia volta, deve ser chamada em caso de beco sem saída
    
    '''
    
    print('os dois sensores ver o verde')
    while robo.sensorCorDireita.color() and robo.sensorCorEsquerda.color() == robo.Color.GREEN:
        robo.bz.drive(100,0)
    robo.bz.stop()
    
    robo.wait(500)

    print('os dois sensores ver a linha preta do beco,')
    while robo.sensorCorDireita.color() and robo.sensorCorEsquerda.color() == robo.Color.BLACK:
        robo.bz.drive(100,0)
    robo.bz.stop()

    print('os sensores passam da linha do beco, e param de ver o preto')
    robo.bz.straight(60)
    robo.bz.stop()
    
    print('robo gira até o sensor da esquerda ver o preto(linha do beco)')
    while robo.sensorCorEsquerda.color() != robo.Color.BLACK:
        robo.motorDireito.run(200)
        robo.motorEsquerdo.run(-200)
    robo.bz.stop()

    robo.wait(500)
    
    print('os sensores passam da linha do beco, e param de ver o preto')
    while robo.sensorCorEsquerda.color() == robo.Color.BLACK:
        robo.motorDireito.run(200)
        robo.motorEsquerdo.run(-200)
    robo.bz.stop()

    robo.wait(500)
    
    print('robo gira até o sensor da esquerda ver o preto(linha do trajeto)')
    while robo.sensorCorEsquerda.color() != robo.Color.BLACK:
        robo.motorDireito.run(200)
        robo.motorEsquerdo.run(-200)
    robo.bz.stop()

    robo.wait(500)
    
    print('robo se ajusta para voltar a seguir linha')
    while robo.sensorCorEsquerda.color() == robo.Color.BLACK:
        robo.motorDireito.run(200)
        robo.motorEsquerdo.run(-200)
    robo.bz.stop()
    robo.bz.turn(- 8)

    robo.wait(500)
    
    
    robo.bz.straight(40)
    alinhar()
                                    
                                    
                                    
                                    


