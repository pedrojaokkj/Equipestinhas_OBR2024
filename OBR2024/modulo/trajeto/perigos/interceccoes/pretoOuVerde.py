#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ....robo import robo
from ...checagens.confirmaCor import confirmaCor
from .preto import preto 
from .verde import verde
from ...checagens.checar_rampa import checarRampa
from ...checagens.rampaCor import rampaCor
from ...checagens.alinhar import alinhar



def pretoOuVerde(sensor:robo.ColorSensor):
    '''Confirma a cor correta com a função confirmar cor e chama a função adequada para a cor lida.
    
    Parameters:
        sensor (ColorSensor) : Sensor que detectou a cor
    '''

    robo.bz.stop()
    if sensor == robo.sensorCorDireita:
        sensor2 = robo.sensorCorEsquerda
    else:
        sensor2 = robo.sensorCorDireita

    if sensor.reflection() <= 14:

        rampa = False
        cores = confirmaCor()

        if rampaCor(cores[2], cores[3], sensorEscuro=sensor ) == True:

            rampa = checarRampa()

        if rampa == True:

            robo.bz.straight(65)
            alinhar()


        else:

            if sensor == robo.sensorCorDireita:

                cor = cores[1]

            else:

                cor = cores[0]



            if cor == robo.Color.BLACK:

                preto(sensor)


            elif cor == robo.Color.GREEN:

                verde(sensor)

            else:
                robo.bz.straight(-30)
                alinhar()
                


    else:
        preto(sensor)