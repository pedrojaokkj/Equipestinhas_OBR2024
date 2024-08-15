#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo
from modulo.trajeto.perigos.interceccoes.preto import preto

def teste():

    while True:
        print(robo.ultrassonicoFrente.distance())

        if robo.ultrassonicoFrente.distance() > 45:
           robo.bz.drive(100,0)
        else:
            
            robo.bz.turn(90)
            
            while robo.sensorCorEsquerda.color() != robo.Color.BLACK:
                robo.bz.drive(-100,0)
            robo.bz.stop()
  
            while robo.ultrassonicoLado.distance() < 150:
                robo.bz.drive(100,0)
            robo.bz.stop()

            robo.bz.straight(160)
            robo.bz.turn(-90)

            while robo.ultrassonicoLado.distance() > 150:
                robo.bz.drive(100,0)
            robo.bz.stop()

            robo.wait(700)

            robo.bz.straight(10)

            while robo.ultrassonicoLado.distance() < 200:
                robo.bz.drive(100,0)
            robo.bz.stop()

            robo.wait(700)

            robo.bz.straight(180)
            robo.bz.turn(-90)

            while robo.sensorCorEsquerda.color() and robo.sensorCorDireita.color() != robo.Color.BLACK:
                robo.bz.drive(100,0)
            robo.bz.stop()

            robo.wait(700)

            while robo.sensorCorEsquerda.color() and robo.sensorCorDireita.color() == robo.Color.BLACK:
                robo.bz.drive(100,0)
            robo.bz.stop()

            robo.bz.straight(40)
            robo.bz.turn(90)
            








