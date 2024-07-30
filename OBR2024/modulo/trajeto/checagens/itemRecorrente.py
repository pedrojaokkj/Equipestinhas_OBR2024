#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
def item_mais_repetido(array):
    contagem = {}
    for item in array:
        if item in contagem:
            contagem[item] += 1
        else:
            contagem[item] = 1
    item_mais_comum = max(contagem, key=contagem.get)
    return item_mais_comum, contagem[item_mais_comum]