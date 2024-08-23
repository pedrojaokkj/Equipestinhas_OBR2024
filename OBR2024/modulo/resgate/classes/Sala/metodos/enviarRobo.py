#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.robo import robo
from ...robo.classeRobo import Robo
from ..funcoesConstrutoras.iniciarMapa import iniciarMapa
from ...Coordenada.coordenada import Coordenada
from ...Mapa.mapa import Mapa
from ...Direcao.direcao import Direcao

from ..metodos.curvaPara import curvaPara





def calcularDistancia(coordenadaFinal : Coordenada, direcaoFinal : Direcao, mapa : Mapa, cooredenadaAtual:Coordenada, direcaoAtual:Direcao, rota : list = []):
    diferencaY = coordenadaFinal.y - cooredenadaAtual.y
    diferencaX = coordenadaFinal.x - cooredenadaAtual.x 


    if diferencaX == 0 and diferencaY == 0 and direcaoAtual.valor == direcaoFinal.valor:
        rota = ['Cabou XD!']


    elif diferencaX == 0 and diferencaY == 0 and direcaoAtual.valor != direcaoFinal.valor:
        rota = [direcaoFinal, 'Cabou XD!']
    
    else:
        p1 = cooredenadaAtual
        p2 = cooredenadaAtual
        possibilidades = []
        
        if diferencaY != 0:
            p1 = mapa.coordenadas[cooredenadaAtual.x - 1][cooredenadaAtual.y - 1 + int(diferencaY/abs(diferencaY))]
            if isinstance(p1, Coordenada): 
                possibilidades.append(p1)




        if diferencaX != 0:
            p2 = mapa.coordenadas[cooredenadaAtual.x - 1 + int(diferencaX/abs(diferencaX))][cooredenadaAtual.y - 1]
            if isinstance(p2, Coordenada):
                possibilidades.append(p2)




            
        



        caminhos = []



        for i,p in enumerate(possibilidades):
            caminhos.append([])
            curvaNecessaria = curvaPara(direcaoAtual, cooredenadaAtual, p)

            caminhos[i] = calcularDistancia(coordenadaFinal, direcaoFinal, mapa, p, curvaNecessaria)

            if curvaNecessaria.valor == direcaoAtual.valor:
                passo = [p]
                caminhos[i].insert(0, passo[0])
            else: 
                passo = [curvaNecessaria, p]
                caminhos[i].insert(0, passo[1])                
                caminhos[i].insert(0, passo[0])




            


        rota = min(caminhos, key=len)

    return rota    
                    


def enviarRobo(self, coordenada : Coordenada, direcao : Direcao):
    mapa = self._mapa
    posicaoAtual = self._robo.coordenadaAtual
    direcaoAtual = self._robo.direcaoAtual

    
    mapaRestringido = Mapa(x = len(mapa.coordenadas), y = len(mapa.coordenadas[0]))

    def restricao(coordenada : Coordenada, mapa : Mapa):
        retorno = False
        maxY = len(mapa.coordenadas[0]) - 1
        maxX = len(mapa.coordenadas) - 1
        quinas = [mapa.coordenadas[0][0], mapa.coordenadas[0][maxY], mapa.coordenadas[maxX][maxY], mapa.coordenadas[maxX][0]]

        if coordenada.comArea == True:
            retorno = True
        elif coordenada in quinas and coordenada.explorada == False:
            retorno = True

        return retorno         
   
    
    

    
    mapaRestringido.coordenadas = [['Coordenada Restringida' if restricao(coorde, mapa) else coorde for coorde in linha] for linha in mapa.coordenadas]
    for linha in mapaRestringido.coordenadas:
        print(' '.join(str((coord.x, coord.y)) if coord  != 'Coordenada Restringida' else 'Restringido' for coord in linha))

    intruncoes = calcularDistancia(coordenada, direcao, mapaRestringido, posicaoAtual, direcaoAtual)


    intruncoesprint = []
    for passo in intruncoes:
        if isinstance(passo, Direcao):
            intruncoesprint.append(passo.valor)
        elif isinstance(passo, Coordenada):
            intruncoesprint.append(passo.posicao)
        else:
            intruncoesprint.append(passo)

    print(intruncoesprint)



    for passo in intruncoes:
        if isinstance(passo, Direcao):
            self._robo.virarAte(passo)

        elif isinstance(passo,  Coordenada):
            self.andarCoordenada()
    
        else:
            print('Chegou')


