#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ....robo import robo
from ...checagens.confirmaCor import confirmaCor
from .preto import preto 
from .verde import verde
from ...checagens.checar_rampa import checarRampa



def pretoOuVerde(sensor:robo.ColorSensor):
    '''Confirma a cor correta com a função confirmar cor e chama a função adequada para a cor lida.
    
    Parameters:
        sensor (ColorSensor) : Sensor que detectou a cor
    '''

    robo.bz.stop()

    if sensor.reflection() <= 14:

        if checarRampa() == True:
            robo.bz.straight(65)

        else:
            cores = confirmaCor()


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
                while robo.sensorCorEsquerda.reflection() > 15:
                    robo.bz.drive(0, 40)

                robo.bz.stop()

                while robo.sensorCorEsquerda.reflection() <= 15:
                    robo.bz.drive(0, -40)

                robo.bz.stop()

                robo.bz.turn(-7)
            


    else:
        preto(sensor)