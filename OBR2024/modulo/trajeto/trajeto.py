#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from pybricks.parameters import Port, Stop, Direction, Button, Color
from ..robo import robo
from ..resgate.salaDeResgate import resgate

from .checagens.entradaSala import entradaDaSala
from .checagens.linhaVermelha import linhaVermelha

from .segueLinha import segueLinha
from .perigos.obstaculo import obstaculo
from .checagens.alinhar import alinhar




#Função do Trajeto Principal
def trajeto():
    while True:
        botoes = len(robo.ev3.buttons.pressed())
        if botoes != 0:
            if botoes == 1:
                break
            else:
                robo.bz.turn(-250)
                while robo.sensorCorDireita.color() == robo.Color.BLACK or robo.bz.distance() > 365:
                    robo.bz.drive(0, 100)

                alinhar()
                break

    robo.ev3.light.off()
    robo.mecanismoDeposito.run_time(-100, 1000)
    robo.garra.run_time(100, 1000)
    final = linhaVermelha()
    while True:

        while True:
            sala = entradaDaSala() 
            final = linhaVermelha()
            if final == True or sala == True:
                robo.bz.stop()
                break
            elif robo.ultrassonicoFrente.distance() < 45:
                obstaculo()
            else:
                segueLinha()


        if sala == True:
            robo.bz.straight(-6)
            sala = entradaDaSala()
            if sala == True:
                resgate()

        elif final == True:
            print("Linha Vermelha")
            break
    
    robo.bz.stop()



