#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo


def verificar_padroes(lista_leituras, tolerancia=10):
    padrao_decrescente = True
    leituras_variaveis = False
    
    for i in range(1, len(lista_leituras)):
        diferenca = lista_leituras[i-1] - lista_leituras[i]
        
        if diferenca < -tolerancia:  # A leitura aumentou significativamente
            padrao_decrescente = False
            leituras_variaveis = True
        elif abs(diferenca) > tolerancia:  # A leitura variou, mas não aumentou
            padrao_decrescente = False
            
    return padrao_decrescente, leituras_variaveis

# Exemplo de uso
leituras = [10.5, 9.8, 9.0, 8.5, 8.7, 8.0]  # Lista de leituras do sensor
decrescente, variavel = verificar_padroes(leituras)

if decrescente:
    print("As leituras estão regularmente decrescentes.")
elif variavel:
    print("As leituras estão variando.")
else:
    print("As leituras não seguem um padrão claro.")