#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________

from ...robo import robo
from .itemRecorrente import item_mais_repetido
from .contarItens import contar_itens


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


    #lógica para o sensor direito
    print('Mais recorrente D: {}'.format(item_mais_repetido(corDireita)))
    contadosD = contar_itens(corDireita)
    print('\n')
    print('Direita')
    for quantidade, cor, percentual in contadosD:
        print("Cor: {} Ocorrências: {} Percentual: {:.2f}%".format(cor, quantidade, percentual))

    print('\n')

    #lógica para o sensor esquerdo
    print('Mais recorrente E: {}'.format(item_mais_repetido(corEsquerda)))

    contadosE = contar_itens(corEsquerda)
    print('\n')
    print('Esquerda')
    for quantidade, cor, percentual in contadosE:
        print("Cor: {} Ocorrências: {} Percentual: {:.2f}%".format(cor, quantidade, percentual))





    corMaisComumDireita = item_mais_repetido(corDireita)[0]   # Extrai apenas a cor
    corMaisComumEsquerda = item_mais_repetido(corEsquerda)[0]    # Extrai apenas a cor


    # Retorna a cor mais comum para ambos os sensores
    return corMaisComumEsquerda, corMaisComumDireita, contadosE, contadosD


