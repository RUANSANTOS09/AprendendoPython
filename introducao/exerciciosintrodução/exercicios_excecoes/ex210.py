while True:
    try:
        password = int(input('Digite uma senha somente com números: '))
    except ValueError:
        print('A senha só deve conter números!! Tente novamente')
    else:
        print('Senha cadstrada com sucesso')
