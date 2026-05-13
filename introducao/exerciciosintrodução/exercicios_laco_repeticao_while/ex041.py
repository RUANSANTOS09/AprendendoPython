numerosNegativos = 0
numerosPositivos = 0
while True:
    num = int(input('Digite um número ou use 0 para encerrar: '))
    if num == 0:
        break
    elif (num < 0):
        numerosNegativos += 1
    else:
        numerosPositivos += 1

print(f'Total de números positivos digitados = {numerosPositivos}\nTotal de números negativos digitados = {numerosNegativos}')