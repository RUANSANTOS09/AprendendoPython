def division(k,j):
    return round(k / j, 2)
if __name__ == '__main__':
 while True:
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    except ValueError:
        print('Erro, foi inserido um caractere diferente de número!!!')
    try:
       result = division(num1,num2)
    except ZeroDivisionError:
        print('Impossível efetuar a divisão por zero')
    else:
        print(f'A divisão entre {num1} e {num2} é {result}')
        break
