while True:
    try:
        user_age = int(input('Digite sua idade: '))
    except ValueError:
        print('Você digitou um caractere diferente de número. Tente novamente!')
    else:
        print(f'Sua idade é {user_age}' )
        break