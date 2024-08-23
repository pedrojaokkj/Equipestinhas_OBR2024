#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo
from ...Mapa.mapa import Mapa
from ...Coordenada.coordenada import Coordenada
from ...Direcao.direcao import Direcao
from .andarEscaneandoY import andarEscaneandoY
from .verificarLado import verificarLado
from .checarSaida import checarSaida
from ...robo.classeRobo import Robo



def escanearFrenteY(robot : Robo, mapa: Mapa):
    ''' Pode alterar o comprimento padrão do mapa e retorna uma lista de Coordenadas da coluna equivalente a entrada.

    Args:
        self()
        mapa(Mapa) : Mapa a ser moldado.
    Returns:
        coordenadas(list[Coordenada]) : lista de Coordenadas da coluna equivalente a entrada.
        mapa(Mapa) : Mapa original, com a sua quantidade de linhas podendo ser alterada.

    '''

    #atribui as variaveis de verificação
    coordenadas = [Coordenada(x = 0, y = 1, explorada = True, entrada = True)] 
    final = False
    y_atual = 1
    paredes_esquerda = []
    paredes_esquerda.append(verificarLado())
    #Vai até o final do eixo X da entrada atualizando os valores
    while True:

        if len(coordenadas) == 4:
            mapa.adcionarY()
            break


        proximoy = andarEscaneandoY(robot, y_atual)

        if proximoy == None:
            break


        coordenadas.append(proximoy)
        

        if proximoy.comArea == True or proximoy.saida == (True, Direcao('Frente')):
            break

        y_atual += 1
        print('y atual == ',y_atual)
        paredes_esquerda.append(verificarLado())
    

    print('Escanear Y concluido')
    


    #Verifica se o tem saida no ultimo ladrilho caso y = 4
    if len(coordenadas) == 4 and coordenadas[len(coordenadas) - 1].comArea() == False and checarSaida() == True:

        coordenadas[len(coordenadas) - 1].saida = (True, Direcao('frente'))

    #atribui um valor para o X das coordenadas de acordo com as leituras acumuladas em paredes_esquerda
    elif paredes_esquerda.count(False) == 1:
        coordenadas[paredes_esquerda.index(False)].saida = (True, Direcao('esquerda'))
        for i, coordenadas in enumerate(coordenadas):
            coordenadas.x = 1

    elif paredes_esquerda.count(False) == 0:
        for i, coordenadas in enumerate(coordenadas):
            coordenadas.x = 1




    print('Voltando')
    robot.virarAte(Direcao('tras'))
    if coordenadas[len(coordenadas)-1].comArea == False and coordenadas[len(coordenadas)-1].saida == [False, None] or coordenadas[len(coordenadas)-1].saida[1].valor != 'frente' :
        robot.ajutarnaParede()
        
    paredes_direita = []
    paredes_direita.append(verificarLado())

    while y_atual != 2:
        #andar 1 ladrilho
        distancia = 280
        robo.bz.straight(distancia)
        paredes_direita.append(verificarLado)
        y_atual -= 1

    print('y=2')
    
    if [coordenada.saida for coordenada in coordenadas].count((True, Direcao('esquerda'))) == 0:

        if paredes_direita.count(False) == 1:
            coordenadas[len(coordenadas) - paredes_esquerda.index(False) - 1].saida = (True, Direcao('direita'))



    robot.virarAte(Direcao('direita'))
    
    return coordenadas, mapa



