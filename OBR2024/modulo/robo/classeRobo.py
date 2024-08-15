#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,
                                 UltrasonicSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


class Robo:
    def __init__(self, 
                 altura : float, 
                 largura : float, 
                 comprimento : float,
                 ev3 : EV3Brick,
                 driveBase : DriveBase, 
                 motorDireito : Motor,
                 motorEsquerdo : Motor,
                 garra : Motor,
                 mecanismoDeposito: Motor,
                 sensorCorEsquerda : ColorSensor,
                 sensorCorDireita : ColorSensor,
                 ultrassonicoLado : UltrasonicSensor,
                 ultrassonicoFrente : UltrasonicSensor,



                 ) -> None:
        '''Classe para representar o robô

        
        
        '''
        self._altura = altura
        self._largura = largura
        self._comprimento = comprimento
        self._ev3 = ev3
        self._bz = driveBase
        self._motorDireito = motorDireito
        self._motorEsquerdo = motorEsquerdo
        self._garra = garra
        self._mecanismoDeposito = mecanismoDeposito
        self._sensorCorEsquerda = sensorCorEsquerda
        self._sensorCorDireita = sensorCorDireita
        self._ultrassonicoLado = ultrassonicoLado
        self._ultrassonicoFrente = ultrassonicoFrente