#Caixas de ovos
#Você tem 53 ovos. Cada caixa comporta 12. Quantas caixas são necessárias para guardar todos?

import math
ovos = 53
caixas = 12
calculo = ovos / caixas
print(f'São necessárias {math.ceil(calculo)} caixas para guardar todos os {ovos} ovos')