import random

sorteio = random.randint(1, 10)
advinhe = int(input('Digite um número e veja se ele foi escolhido pelo computador: '))
if advinhe == sorteio:
    print(f'O número sorteado é {sorteio}, parabéns você acertou!!!!!!!!')
else:
    print(f'O número sorteado era o {sorteio} e você errou :(')
print(sorteio)
