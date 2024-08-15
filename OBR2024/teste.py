#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo
from modulo.trajeto.perigos.interceccoes.preto import preto

def teste():
    print('os dois sensores ver o verde')
    while robo.sensorCorDireita.color() and robo.sensorCorEsquerda.color() == robo.Color.GREEN:
        robo.bz.drive(100,0)
    robo.bz.stop()
    
    print('os dois sensores ver a linha preta do beco,')
    while robo.sensorCorDireita.color() and robo.sensorCorEsquerda.color() == robo.Color.BLACK:
        robo.bz.drive(100,0)
    robo.bz.stop()
    
    print('os sensores passam da linha do beco, e param de ver o preto')
    robo.bz.straight(100)
    robo.bz.stop()
    
    print('robo gira até o sensor da esquerda ver o preto(linha do beco)')
    while robo.sensorCorEsquerda.color() != robo.Color.BLACK:
        robo.motorEsquerdo.run(-100)
    robo.bz.stop()

    robo.wait(1000)
    
    print('os sensores passam da linha do beco, e param de ver o preto')
    while robo.sensorCorEsquerda.color() == robo.Color.BLACK:
        robo.motorEsquerdo.run(-100)
    robo.bz.stop()
    
    print('robo gira até o sensor da esquerda ver o preto(linha do trajeto)')
    while robo.sensorCorEsquerda.color() != robo.Color.BLACK:
        robo.motorEsquerdo.run(-100)
    robo.bz.stop()
    
    print('robo se ajusta para voltar a seguir linha')
    while robo.sensorCorEsquerda.color() == robo.Color.BLACK:
        robo.motorEsquerdo.run(-100)
    robo.bz.stop()

    robo.wait(1000)    