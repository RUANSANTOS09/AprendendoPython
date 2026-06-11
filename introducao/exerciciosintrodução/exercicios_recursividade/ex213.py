def count(num, counter=1 ):
    if counter > num:
        return
    print(counter)
    count(num, counter + 1)





if __name__ == '__main__':
    try:
        num = int(input('Digite um numero maior que zero e que não possua letras: '))
        if num < 1:
            print('Error\nO número não pode ser 0')
        else:
            count(num)
    except ValueError:
        print('O caractere fornecido não é um número.')

