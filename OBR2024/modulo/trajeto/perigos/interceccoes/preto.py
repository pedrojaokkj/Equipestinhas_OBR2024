#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ....robo import robo
from ...checagens.alinhar import alinhar

def preto(sensor:robo.ColorSensor):
    '''Segue o protocolo para quando um sensor detecta preto.
    
    Parameters:
        sensor (ColorSensor) : Sensor que detectou a cor preta
    '''

    print("Função Preto")

    robo.bz.stop()


    #Atribui as variáveis de acordo com o sensor passado como parametro
    if sensor == robo.sensorCorDireita:
        lado = 1
        motor = robo.motorDireito
        motor2 = robo.motorEsquerdo
        sensor2 = robo.sensorCorEsquerda
    else:
        lado = -1
        motor = robo.motorEsquerdo
        motor2 = robo.motorDireito
        sensor2 = robo.sensorCorDireita




    #Vira em caso de preto total 
    print(sensor.reflection())
    if sensor.reflection() <= 15:


        print("virar")

        robo.bz.stop()
        robo.bz.straight(40)
        robo.bz.stop()
        motor2.reset_angle(0)

        #vira o robô verificando se existe linha para a frente
        while motor2.angle() < 50 and sensor2.reflection() > 15:
            robo.bz.drive(0, 40 * lado)

        robo.bz.stop()
        print(sensor2.reflection())

        if sensor2.reflection() < 15:

            print('Linha frontal detectada, Alterando rota.')
            while sensor2.reflection() <= 15:
                robo.bz.drive(0, -40 * lado)

            robo.bz.turn(-6 * lado)
            robo.bz.stop()
            robo.bz.straight(20)
        

        else:

            print("Procurando Linha...")
            while motor2.angle() >= 0:
                robo.bz.drive(0, -40 * lado)
            
            robo.bz.stop()
            robo.bz.straight(10)

            while sensor2.reflection() > 15:
                robo.bz.drive(0, 40 * lado)

            robo.bz.stop()

            alinhar()

        
    #ajusta o robô em caso de invasão leve na linha
    else:


        alinhar()        
        # robo.bz.stop()
        # while sensor.reflection() < 65:    
        #     motor.run(-35)

        # motor.stop() 
        # robo.bz.straight(-6)
        # robo.bz.stop()


    return