#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
def item_mais_repetido(array):
    '''Verifica se o Robô chegou na sala de resgate.
        
    Returns:
        retorno (boolean): Retorna se o robô está na sala de resgate(True) ou não(False)
    '''
        
    contagem = {}
    for item in array:
        if item in contagem:
            contagem[item] += 1
        else:
            contagem[item] = 1
    item_mais_comum = max(contagem, key=contagem.get)
    return item_mais_comum, contagem[item_mais_comum]