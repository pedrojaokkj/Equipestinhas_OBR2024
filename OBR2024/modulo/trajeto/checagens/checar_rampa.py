#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ...robo import robo

def checarRampa():
    print('checando rampa')
    bz = robo.bz
    
    bz.stop()
    bz.reset()
    print(robo.motorDireito.angle(), robo.motorEsquerdo.angle())
    bz.straight(40)
    print(robo.motorDireito.angle(), robo.motorEsquerdo.angle())
    bz.stop()
    robo.motorDireito.reset_angle(0)
    robo.motorEsquerdo.reset_angle(0)
    print(robo.motorDireito.angle(), robo.motorEsquerdo.angle())
    bz.stop()
    while robo.motorDireito.angle() > -60:
        print(robo.motorDireito.angle())
        robo.motorDireito.run(-45)
        robo.motorEsquerdo.run(-45)
    robo.motorDireito.stop()
    robo.motorEsquerdo.stop()
    robo.motorDireito.reset_angle(0)
    robo.motorEsquerdo.reset_angle(0)
    robo.wait(3000)
    print(robo.motorDireito.angle(), robo.motorEsquerdo.angle())

    
    leituraE = robo.motorEsquerdo.angle()
    leituraD = robo.motorDireito.angle()

    if leituraD > 20 and leituraE > 20:
        retorno = True
    else:
        retorno = False
        bz.straight(-22)
        
    
    return retorno
