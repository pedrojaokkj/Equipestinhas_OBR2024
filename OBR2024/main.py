#!/usr/bin/env pybricks-micropython

#Importações
#______________________________________________________________________________________________________________________________________
from modulo.trajeto.trajeto import trajeto
from teste import teste
from modulo.robo import robo

from modulo.trajeto.interceccoes.verde import verde

# Chamada da Função Principal
# if __name__ == "__main__":
#     trajeto()


# Chamada da Função de Testes
if __name__ == "__main__":
    verde(robo.sensorCorDireita)