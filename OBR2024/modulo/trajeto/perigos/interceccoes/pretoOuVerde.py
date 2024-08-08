#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ....robo import robo
from ...checagens.confirmaCor import confirmaCor
from .preto import preto 
from .verde import verde



def pretoOuVerde(sensor:robo.ColorSensor):
    '''Confirma a cor correta com a função confirmar cor e chama a função adequada para a cor lida.
    
    Parameters:
        sensor (ColorSensor) : Sensor que detectou a cor
    '''

    if sensor.reflection() <= 8:

        cores = confirmaCor()


        if sensor == robo.sensorCorDireita:

            cor = cores[2]

        else:

            cor = cores[1]



        if cor == robo.Color.BLACK:

            preto(sensor)


        elif cor == robo.Color.GREEN:

            verde(sensor)
        


    else:
        preto(sensor)