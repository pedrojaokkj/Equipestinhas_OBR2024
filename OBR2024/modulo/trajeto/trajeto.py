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




#Função do Trajeto Principal
def trajeto():
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
            resgate()

        elif final == True:
            print("Linha Vermelha")
            break
    
    robo.bz.stop()



