nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
for x in range(1, 11):
    if x % 2 == 0 and idade < 18:
        print(f'{x} - MENOR DE IDADE')
    elif x % 2 == 0 and idade >= 18:
        print(f'{x} - MAIOR DE IDADAE')
    else:
        print(f'{x} {nome}')