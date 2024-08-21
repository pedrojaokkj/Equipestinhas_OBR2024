#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo


def check_rampa(colors, percentual):
    if robo.Color.WHITE in colors and percentual[colors.index(robo.Color.WHITE)] == 100:
        return False
    if robo.Color.WHITE not in colors or percentual[colors.index(robo.Color.WHITE)] < 10:
        return True
    if None in colors:
        return True
    if robo.Color.BLUE in colors and percentual[colors.index(robo.Color.BLUE)] > 50:
        return True
    return False



def check_rampa2(cE, cD, pE, pD):
    if None in cE or None in cD:
        return True
    if robo.Color.BLUE in cE and pE[cE.index(robo.Color.BLUE)] > 40 or robo.Color.BLUE in cD and pD[cD.index(robo.Color.BLUE)] > 40:
        return True
    
    return False




def rampaCor(infoEsq: list[tuple], infoDir: list[tuple], sensorEscuro: robo.ColorSensor = robo.sensorCorDireita, dois : bool= False) -> bool:
    """Recebe listas com leituras dos sensores de cor, e retorna se existe a possibilidade de o robo estar em uma rampa

    Args:
        infoDir (list): Lista de leituras do sensor direito
        infoEsq (list): Lista de leituras do sensor esquerdo
        sensorEscuro (ColorSensor): Em caso de leitura unilateral, deve ser passado o motor que detectou preto ou verde

    Returns:
        bool: A possibilidade de estar em uma rampa (True se sim, False se não)
    """

    if not infoDir or not infoEsq:
        raise ValueError("Listas de leituras devem ser não vazias")

    vezesE, colorsE, percentualE = zip(*infoEsq)
    vezesD, colorsD, percentualD = zip(*infoDir)



    if dois == True:
        retorno = check_rampa2(colorsE, colorsD, percentualE ,percentualD)
    else:
        if sensorEscuro == robo.sensorCorDireita:
            retorno = check_rampa(colorsE, percentualE)
        else:
            retorno = check_rampa(colorsD, percentualD)

    return retorno

