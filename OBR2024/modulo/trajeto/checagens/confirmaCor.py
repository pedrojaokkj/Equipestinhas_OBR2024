#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________

from ...robo import robo
from .itemRecorrente import item_mais_repetido




def confirmaCor():
    corEsquerda = []  #array que armazenará as leituras do sensor esquerdo
    corDireita = []   #array que armazenará as leituras do sensor direito


    #vai pra frente armazenando as leituras
    for i in range(85):
        robo.bizzoru.drive(25,0)
        corEsquerda.append(robo.sensorCorEsquerda.color())
        corDireita.append(robo.sensorCorDireita.color())
        robo.wait(1)

    #volta armazenando as leituras
    for i in range(100):
        robo.bizzoru.drive(-25,0)
        corEsquerda.append(robo.sensorCorEsquerda.color())
        corDireita.append(robo.sensorCorDireita.color())
        robo.wait(1)

    robo.bizzoru.stop()

    # Encontra os itens mais comuns
    corMaisComumEsquerda = item_mais_repetido(corEsquerda)[0]  # Extrai apenas a cor
    corMaisComumDireita = item_mais_repetido(corDireita)[0]    # Extrai apenas a cor

    # Retorna a cor mais comum para ambos os sensores
    return [corMaisComumEsquerda, corMaisComumDireita]