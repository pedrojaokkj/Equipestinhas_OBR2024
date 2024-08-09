#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo
from modulo.trajeto.perigos.interceccoes.preto import preto

def teste(sensor:robo.ColorSensor):
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
    print(sensor.color())
    if sensor.reflection() <= 15:


        print("virar")

        robo.bz.straight(50)
        robo.bz.stop()
        motor2.reset_angle(0)

        #vira o robô verificando se existe linha para a frente
        while motor2.angle() < 27 and sensor2.reflection() > 15:
            robo.bz.drive(0, 40 * lado)

        robo.bz.stop()
        print(sensor2.reflection())
        if sensor2.reflection() < 15:

            print('Linha frontal detectada, Alterando rota.')

            while sensor2.reflection() <= 15:
                robo.bz.drive(0, -40 * lado)

            robo.bz.stop()
            robo.bz.straight(20)
        

        else:

            robo.bz.straight(-20)
            while sensor2.reflection() > 15:
                robo.bz.drive(0, 40 * lado)

            robo.bz.stop()

            while sensor2.reflection() <= 15:
                robo.bz.drive(0, -40 * lado)

            robo.bz.stop() 



