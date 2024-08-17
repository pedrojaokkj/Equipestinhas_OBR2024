#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo


def rampaCor(infoDir : list, infoEsq : list, sensorEscuro : robo.ColorSensor = robo.sensorCorDireita, dois = False):
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


    if dois == True:

        if None in infoDir or None in infoEsq:
            rampa = True

        if infoEsq[0][1] == robo.Color.BLUE or infoDir[0][1] == robo.Color.BLUE:
            rampa = True

        if robo.sensorCorDireita.reflection() > 15 or robo.sensorCorDireita.reflection() > 15:
            rampa = True

        




    elif sensorEscuro == robo.sensorCorDireita:
        vezesE, colorsE, percentualE = infoEsq

        if robo.Color.WHITE not in colorsE or percentualE[colorsE[robo.Color.WHITE]] < 10:
            rampa = True

        if None in colorsE:
            rampa = True
        
        if robo.Color.BLUE in colorsE and percentualE[colorsE[robo.Color.BLUE]] > 50:
            rampa = True

    else:
        vezesD, colorsD, percentualD = infoDir
        if robo.Color.WHITE not in colorsD or percentualD[colorsD[robo.Color.WHITE]] < 10:
            rampa = True

        if None in colorsD:
            rampa = True
        
        if robo.Color.BLUE in colorsD and percentualD[colorsD[robo.Color.BLUE]] > 50:
            rampa = True
 


    return rampa
