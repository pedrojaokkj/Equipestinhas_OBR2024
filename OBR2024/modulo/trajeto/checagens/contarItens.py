#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo



def contar_itens(lista):
  """Conta a quantidade de vezes que cada item aparece em uma lista e retorna uma lista de tuplas (item, quantidade).

  Args:
    lista: A lista para analisar.

  Returns:
    Uma lista de tuplas (item, quantidade), onde cada tupla representa um item
    da lista e a quantidade de vezes que ele aparece.
  """

  contagem = {}
  for item in lista:
    if item in contagem:
      contagem[item] += 1
    else:
      contagem[item] = 1

  return [(quantidade, item, quantidade/len(lista) * 100) for item, quantidade in contagem.items()]
