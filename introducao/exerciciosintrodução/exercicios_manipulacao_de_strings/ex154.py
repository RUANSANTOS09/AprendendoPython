frase = str(input('Digite uma frase: '))
lista_frase = frase.split()
contador_palavra = 0
for contador, palavra in enumerate(frase.split(), start=1):
    contador_palavra += 1
    print(f'{contador}. {palavra}')
