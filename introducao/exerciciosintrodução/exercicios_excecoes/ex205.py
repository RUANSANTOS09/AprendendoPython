while True:
    try:
        positve_number = int(input('Digite um número positivo: '))
        if positve_number < 0:
           raise ValueError(f'Apenas númervos são permitidos. Tente novamente')
    except ValueError as erro:
        print(erro)
    else:
        print(positve_number)
        break