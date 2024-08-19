#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo



def contar_itens(lista):
  """Conta a quantidade de vezes que cada item aparece em uma lista e retorna uma lista de tuplas (item, quantidade).

  Args:
    lista: A lista para analisar.

  Returns:
    Uma lista de tuplas (item, quantidade, percentual), onde cada tupla representa um item
    da lista e a quantidade de vezes que ele aparece.
  """

  contagem = {}
  for item in lista:
    if item in contagem:
      contagem[item] += 1
    else:
      contagem[item] = 1


  # Cria a lista de tuplas (quantidade, item, percentual)
  resultado = [(quantidade, item, quantidade/len(lista) * 100) for item, quantidade in contagem.items()]

  # Ordena a lista com base na quantidade em ordem decrescente
  resultado.sort(key=lambda x: x[0], reverse=True)

  return resultado
