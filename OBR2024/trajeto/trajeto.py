#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from pybricks.parameters import Port, Stop, Direction, Button, Color
import OBR2024.robo.robo as robo
import OBR2024.resgate.salaDeResgate as salaDeResgate

from segueLinha import segueLinha
from obstaculo import obstaculo




#Função do Trajeto Principal
def trajeto():
    while entradaDaSala() == False and linhaVermelha() == False:
        if robo.ultrassonicoFrente.distance() < 45:
            obstaculo()
        else:
            segueLinha()

    if linhaVermelha() == True:
        acabou()
    else:
        salaDeResgate.resgate()


# Verifica se o robô está na entrada da sala
def entradaDaSala():
    return False


# Verifica se o robô está na linha vermelha
def linhaVermelha():
    retorno = robo.sensorCorDireita.color() == Color.RED and robo.sensorCorEsquerda.color() == Color.RED
    return retorno


# Finaliza o Trajeto
def acabou():
    print('Acabou')
    robo.ev3.light.off() 