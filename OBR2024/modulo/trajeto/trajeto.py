#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from pybricks.parameters import Port, Stop, Direction, Button, Color
from ..robo import robo
from ..resgate.salaDeResgate import resgate

from .checagens.entradaSala import entradaDaSala
from .checagens.linhaVermelha import linhaVermelha

from .segueLinha import segueLinha
from .obstaculo import obstaculo




#Função do Trajeto Principal
def trajeto():
    while True:
        while linhaVermelha() == False and entradaDaSala() == False:
            if robo.ultrassonicoFrente.distance() < 45:
                obstaculo()
            else:
                segueLinha()

        if entradaDaSala() == True:        
            resgate()
        elif linhaVermelha():
            print("Linha Vermelha")
            break
    
    robo.bizzoru.stop()



