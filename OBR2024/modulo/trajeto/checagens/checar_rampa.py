#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo
from .itemRecorrente import item_mais_repetido
from .contarItens import contar_itens

def checarRampa():
    '''Verifica se o Robô está em uma rampa

    Returns:
        retorno(boolean): True para caso o robô esteja na rampa, False para caso não esteja
    '''


    print('Checando rampa...')
    bz = robo.bz
    
    bz.stop()
    bz.reset()


    bz.straight(40)
    bz.stop()

    robo.motorDireito.reset_angle(0)
    robo.motorEsquerdo.reset_angle(0)

    print(robo.motorDireito.angle(), robo.motorEsquerdo.angle())
    bz.stop()

    coresD = []
    coresE = []
    while robo.motorDireito.angle() > -60:
        coresD.append(robo.sensorCorDireita.color())
        coresE.append(robo.sensorCorEsquerda.color())
        robo.motorDireito.run(-65)
        robo.motorEsquerdo.run(-65)


    robo.motorDireito.stop()
    robo.motorEsquerdo.stop()

    robo.motorDireito.reset_angle(0)
    robo.motorEsquerdo.reset_angle(0)
    robo.wait(1100)

    print(robo.motorDireito.angle(), robo.motorEsquerdo.angle())

    

    
    leituraE = robo.motorEsquerdo.angle()
    leituraD = robo.motorDireito.angle()

    if leituraD < -20 and leituraE < -20:
        retorno = True
    else:
        retorno = False
        bz.straight(-22)

    print('Rampa : {}'.format(retorno))



    
    return retorno
