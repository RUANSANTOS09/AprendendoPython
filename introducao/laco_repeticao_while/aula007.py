nome = None

while True:
    nome = input('Digite seu nome, ou x para parar: ')
    if(nome == 'x' or nome == 'X'):
        break
    else:
       print(f'Bem vindo, {nome}!')

print('Até logo!')