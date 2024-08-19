#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo


def rampaCor(infoDir : list[tuple], infoEsq : list[tuple], sensorEscuro : robo.ColorSensor = robo.sensorCorDireita):
    '''Recebe listas com leituras dos sensores de cor, e retorna se existe a possibilidade de o robo estar em uma rampa

    Args:
        infoDir(list) : Lista de leituras do sensor direito
        infoEsq(list) : Lista de leituras do sensor esquerdo
        sensorEscuro(ColorSensor) : Em caso de leitura unilateral, deve ser passado o motor que detectou preto ou verde
        dois(boolean) : Caso seja definido como True a função atribui a verificação aos dois sensores

    Returns:
        rampa(boolean) : A possibilidade de estar em uma rampa
    
    
    '''

    rampa = False
    vezesE, colorsE, percentualE = zip(*infoEsq)
    vezesD, colorsD, percentualD = zip(*infoDir)


    if sensorEscuro == robo.sensorCorDireita:

        if robo.Color.WHITE not in colorsE or percentualE[colorsE[robo.Color.WHITE]] < 10:
            rampa = True

        if None in colorsE:
            rampa = True
        
        if robo.Color.BLUE in colorsE and percentualE[colorsE[robo.Color.BLUE]] > 50:
            rampa = True

    else:
        
        if robo.Color.WHITE not in colorsD or percentualD[colorsD[robo.Color.WHITE]] < 10:
            rampa = True

        if None in colorsD:
            rampa = True
        
        if robo.Color.BLUE in colorsD and percentualD[colorsD[robo.Color.BLUE]] > 50:
            rampa = True
 


    return rampa
