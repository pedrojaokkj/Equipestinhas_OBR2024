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
    while entradaDaSala() == False and linhaVermelha() == False:
        if robo.ultrassonicoFrente.distance() < 45:
            obstaculo()
        else:
            segueLinha()
            

    if linhaVermelha() == True:
        robo.bizzoru.stop()
    else:
        resgate()
        trajeto()



