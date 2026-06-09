class NumberNegativeError(Exception):
    pass
while True:
    try:
        num = int(input('Digite um número positivo: '))
        if num < 0:
            raise NumberNegativeError
    except NumberNegativeError:
        print('Número negativo!! Utilize apenas números postivos. Tente novamente')
    else:
        print(num)
        break
