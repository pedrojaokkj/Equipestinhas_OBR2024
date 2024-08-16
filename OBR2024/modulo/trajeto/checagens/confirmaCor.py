#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________

from ...robo import robo
from .itemRecorrente import item_mais_repetido


def confirmaCor():
    '''Faz o robô ir para frente e para trás checando a cor que mais se repete na area onde o robô se localiza.

    Returns:
        corMaisComumEsquerda (Color) : Cor mais recorrente no sensor da esquerda
        corMaisComumDireita (Color) : Cor mais recorrente no sensor da direita
    '''

    robo.bz.stop()

    print('Confirmando Cor...')

    corEsquerda = []  #array que armazenará as leituras do sensor esquerdo
    corDireita = []   #array que armazenará as leituras do sensor direito


    #vai pra frente armazenando as leituras
    for i in range(85):
        robo.bz.drive(15,0)
        corEsquerda.append(robo.sensorCorEsquerda.color())
        corDireita.append(robo.sensorCorDireita.color())
        robo.wait(1)

    #volta armazenando as leituras
    for i in range(100):
        robo.bz.drive(-15,0)
        corEsquerda.append(robo.sensorCorEsquerda.color())
        corDireita.append(robo.sensorCorDireita.color())
        robo.wait(1)

    robo.bz.stop()

    # Encontra os itens mais comuns
    verdesD = [cor for cor in corDireita if cor == robo.Color.GREEN]
    verdesE = [cor for cor in corEsquerda if cor == robo.Color.GREEN]

    if len(verdesD) / len(corDireita) > 0.20:
        corMaisComumDireita = robo.Color.GREEN
    else:
        corMaisComumDireita = item_mais_repetido(corDireita)[0]    # Extrai apenas a cor

    if len(verdesE) / len(corEsquerda) > 0.20:
        corMaisComumEsquerda = robo.Color.GREEN
    else:
        corMaisComumEsquerda = item_mais_repetido(corEsquerda)[0]  # Extrai apenas a cor

    print("Esquerda {}".format(len(verdesE) / len(corEsquerda)))
    print("Direita: {}".format(len(verdesD) / len(corDireita)))

    print("Cores: {}, {}".format(corMaisComumEsquerda, corMaisComumDireita))

    # Retorna a cor mais comum para ambos os sensores
    return corMaisComumEsquerda, corMaisComumDireita


