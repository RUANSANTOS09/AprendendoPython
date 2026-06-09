from math import sqrt
while True:
    try:
        num = int(input('Digite um número: '))
    except ValueError:
        print('Foi detectado um caractere diferente de número. Tente novamente')
    else:
        print(f'A raiz quadrada de {num} é {sqrt(num)} ')
        break
    finally:
        print('Fim do programa')