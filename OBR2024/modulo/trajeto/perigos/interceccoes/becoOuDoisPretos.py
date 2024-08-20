#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ....robo import robo
from ...checagens.confirmaCor import confirmaCor
from .doisPretos import doisPretos
from .becoSemSaida import becoSemSaida
from .verde import verde
from ...checagens.checar_rampa import checarRampa
from ...checagens.rampaCor import rampaCor
from ...checagens.alinhar import alinhar


def becoOuDoisPretos():
    '''Confere se o robô está em uma intercecção comum ou em um beco sem saída e chama a função apropriada.
    
    '''

    print("Conferindo Intercecção(beco ou dois pretos)...")
    bz = robo.bz




    rampa = checarRampa()

    
    if rampa == True:
        bz.straight(65)
        alinhar()

    else:
        bz.straight(-30)

        

        #alinhar o robô

        alinhar()

        robo.bz.reset()

        while robo.sensorCorEsquerda.reflection() > 15 and robo.sensorCorDireita.reflection() > 15 and robo.bz.distance() <=40:
            robo.bz.drive(35, 0)
        
        print(robo.sensorCorEsquerda.reflection())
        print(robo.sensorCorDireita.reflection())
        print(robo.bz.distance())
        bz.stop()


        cores = confirmaCor()
        
        vezesE, colorsE, percentualE = zip(*cores[2])
        vezesD, colorsD, percentualD = zip(*cores[3]) 

        if cores[:2] == (robo.Color.BLACK, robo.Color.BLACK):
            doisPretos()
        elif cores[:2] == (robo.Color.GREEN, robo.Color.GREEN):
            becoSemSaida()
        else:
            bz.straight(-30)
            alinhar()
