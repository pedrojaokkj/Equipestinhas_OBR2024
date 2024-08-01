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



#______________________________________________________________________________________________________________________________________


# Incializando o robô e seus componentes
#______________________________________________________________________________________________________________________________________
ev3 = EV3Brick()

motorDireito = Motor(
    Port.B, positive_direction=Direction.COUNTERCLOCKWISE, gears=None) # <-- Motor da roda direita

motorEsquerdo = Motor(
    Port.A, positive_direction=Direction.COUNTERCLOCKWISE, gears=None) # <-- Motor da roda esquerda


garra = Motor(Port.C)

mecanismoDeposito = Motor(Port.D)


bizzoru = DriveBase(motorEsquerdo, motorDireito, wheel_diameter=68.8, axle_track=170) # <-- Iniciando o DriveBase5
bizzoru.settings(straight_speed=200, turn_rate=150)


sensorCorEsquerda = ColorSensor(Port.S1)
sensorCorDireita = ColorSensor(Port.S2)

ultrassonicoLado = UltrasonicSensor(Port.S3)
ultrassonicoFrente = UltrasonicSensor(Port.S4)



















