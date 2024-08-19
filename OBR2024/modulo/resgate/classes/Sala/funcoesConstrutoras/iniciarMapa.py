#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo.robo import robo
from ...robo.classeRobo import Robo
from ...Coordenada.coordenada import Coordenada
from ...Mapa.mapa import Mapa



def iniciarMapa(mapa : Mapa):
    ''' Faz as atribuções das propriedades no mapa da sala, centraliza o robô e retorna o mapa atualizado

    
    Returns:
        mapa(Mapa) : Mapa da sala iniciada.
    '''
    coordenadas_y_entrada = []

    
    print("Alinhando...")
    #alinhar

    print("Entrando na sala...")
    #ir até ladrilho inicial

    
    


    


    #sempre se sala.frenteEsperada == False -> capturar


        #robo entra no ladrilho x=? y=1


        #ladrilho

    

    largura = 3 #ou 4
    if largura == 4:
        mapa.adcionarY()


    comprimento = 3 #ou 4
    if comprimento == 4:
        mapa.adcionarX()



    return (mapa)