#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo.robo import robo
from ..pedacoParede import PedacoDeParede
from..parede import Parede
from ....robo.classeRobo import Robo
from ..area import AreaDeResgate

def escanearSala():
    ''' Faz as atribuções das propriedades da sala, centraliza o robô e retorna as propriedades

    
    Returns:
        largura(int) : Largura da sala( 900mm ou 1200mm )
        comprimento(int) : Comprimento da sala( 900mm ou 1200mm )
        entrada(PedacoDeParede) : Parte da sala onde a entrada se encontra
        saida(tuple(Boolean, PedacoDeParede)) : Se a saida for previamente identificada, retorna True e sua posição, se não, retorna False e Undefined.  
    '''

    print("Escaneando Sala...")

    largura = 90
    comprimento = 90
    entrada = PedacoDeParede() 
    saida = (True, PedacoDeParede())
    area1 = AreaDeResgate("D", 'A')
    area2 = AreaDeResgate("D", 'C')



    return (largura, comprimento, entrada, saida, area1, area2)