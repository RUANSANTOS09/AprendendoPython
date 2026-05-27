palavra = str(input('Digite uma palavra: ')).upper()
primeira_letra = palavra[0]
ultima_letra = palavra[-1]
if primeira_letra == ultima_letra:
    print(f'A palavra "{palavra}" começa e termina com a letra "{primeira_letra}"')
else:
    print(f'A palavra "{palavra}" começa com a letra "{primeira_letra}" e termina com a letra "{ultima_letra}"')