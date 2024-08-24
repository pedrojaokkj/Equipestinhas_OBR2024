#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from .....robo import robo
from ...robo.classeRobo import Robo
from ...Coordenada.coordenada import Coordenada
from ...Mapa.mapa import Mapa
from ...Direcao.direcao import Direcao

from .....trajeto.checagens.alinhar import alinhar


def sair(self):
    
    mapa = self._mapa
    saida = self._saida

    if saida[1].valor == None:

        self.explorar()
        mapa = self._mapa
        saida = self._saida

        if saida[1].valor == None:
            return


    self.enviarRobo(saida[0], saida[1])
    while robo.sensorCorDireita.reflection() < 18:
        robo.bz.drive(60, 0)
    robo.bz.stop()

    robo.bz.straight(40)
    alinhar()


