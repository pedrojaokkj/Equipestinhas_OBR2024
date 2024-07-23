#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,
                                 UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



#______________________________________________________________________________________________________________________________________


# Incializando o robô e seus componentes
#______________________________________________________________________________________________________________________________________
ev3 = EV3Brick()

motorDireito = Motor(
    Port.A, positive_direction=Direction.COUNTERCLOCKWISE, gears=None) # <-- Motor da roda direita

motorEsquerdo = Motor(
    Port.D, positive_direction=Direction.COUNTERCLOCKWISE, gears=None) # <-- Motor da roda esquerda


meuRobo = DriveBase(motorEsquerdo, motorDireito, wheel_diameter=68.8, axle_track=160) # <-- Iniciando o DriveBase5

sensorCorEsquerda = ColorSensor(Port.S1)
sensorCorDireita = ColorSensor(Port.S4)

sensorUltrassonico = UltrasonicSensor(Port.S3)
sensorGyro = GyroSensor(Port.S2)

















