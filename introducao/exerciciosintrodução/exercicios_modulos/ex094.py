#Juros compostos
#R$ 1000 aplicados a 5% ao ano durante 3 anos. Calcule o montante final.

import math
montante_aplicado = 1000
taxa = 1 + 0.05
calc = montante_aplicado * math.pow(taxa,3)
print(calc)