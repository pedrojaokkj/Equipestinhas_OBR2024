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
import os


def tocar():
    sound = robo.SoundFile().EV3

    robo.ev3.speaker.play_file(sound)