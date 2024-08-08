#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from ....robo import robo

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
    if sensor.reflection() <= 8:


        print("virar")

        robo.bz.straight(40)
        robo.bz.stop()
        motor2.reset_angle()

        #vira o robô verificando se existe linha para a frente
        while motor2.angle() < () and sensor2.reflection() > 50:
            motor2.run(100) 

        motor2.stop()

        if sensor2.reflection() < 50:

            print('Linha frontal detectada, Alterando rota.')

            motor2.run_target(100, -motor2.angle())
            robo.bz.straight(40)
        

        else:


            motor2.run(200)
            motor.run(-200) 
            while True:

                if sensor2.reflection() <= 40:
                    motor2.stop()
                    motor.stop()
                    break


            while True:
                motor.run(100)
                motor2.run(-100)
                if sensor.reflection() <= 40:
                    robo.bz.stop()
                    break    

            robo.bz.turn(13 * lado)



        

        
    #ajusta o robô em caso de invasão leve na linha
    else:
        print("ajustar")
        robo.bz.turn(5 * lado)        
    