#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
import modulo.robo.robo as robo




def leituraMotores():
    md = robo.motorDireito
    me = robo.motorEsquerdo
    me.reset_angle(0)
    md.reset_angle(0)
    ultimaLeituraD =me.angle()
    ultimaLeituraE =md.angle()
    while True:
        if me.angle() != ultimaLeituraE:
            print("Esquerda:{}".format(me.angle()))
        if md.angle() != ultimaLeituraD:
            print("Direita:{}".format(md.angle()))

        if robo.ev3.buttons.pressed() != []:
            me.reset_angle(0)
            md.reset_angle(0)
            print('Leituras Zeradas')
            robo.wait(500)
   
        ultimaLeituraE =me.angle()
        ultimaLeituraD =md.angle()