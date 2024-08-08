#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ....robo import robo

def becoSemSaida():
    '''Faz o robô dar meia volta, deve ser chamada em caso de beco sem saída
    
    '''
    
    print("meia volta")

    while True:
        print('os dois sensores detectam o verde')
        if robo.sensorCorEsquerda.color() and robo.sensorCorDireita.color() == robo.Color.GREEN:
            print('os dois sensores detectam o preto, e o robo anda 8cm para frente')
            while robo.sensorCorEsquerda.color() and robo.sensorCorDireita.color() != robo.Color.BLACK:
                robo.bz.drive(80)
            
            else:
                robo.bz.straight(50)
                print(" robo gira até o sensor da esquerda ver o preto")
                while robo.sensorCorEsquerda.color() != robo.Color.BLACK:
                    robo.bz.stop()
                    robo.motorEsquerdo.run(-50)
                
                else:
                    robo.wait(2000)
                    robo.motorEsquerdo.angle(-150)
                    print(" robo gira até o sensor da esquerda ver o preto(linha)")
                    while robo.sensorCorEsquerda.color() != robo.Color.BLACK:
                        robo.motorEsquerdo.run(-50)

                    else:
                        robo.wait(2000)
                        robo.motorEsquerdo.angle(-150)



        break
