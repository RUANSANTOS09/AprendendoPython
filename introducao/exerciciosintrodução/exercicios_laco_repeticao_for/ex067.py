nome = input('Digite seu nome: ')
vogais = 'aeiouAEIOU'
posicao = 0
for letra in nome:
    posicao += 1
    if letra in vogais:
        continue
    print(f'{posicao} - {letra}')
