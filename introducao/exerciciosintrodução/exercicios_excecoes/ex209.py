def sum(k,j):
    return k + j
if __name__ == '__main__':
    while True:
        try:
            num1 = int(input('Digite um número inteiro: '))
            num2 = int(input('Digite outro número inteiro: '))
        except ValueError:
            print('Só é permitido números inteiros. Tente novamente.')
        else:
            result = sum(num1,num2)
            print(result)
            break
        finally:
            print('Calculo Finalizado')
