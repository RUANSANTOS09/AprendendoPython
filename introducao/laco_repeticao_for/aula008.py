
palavra = 'Ruan'
for letra in palavra:
    print(letra)

for numero in range(10):
    print(numero)

nome = input('Qual o seu nome? ')
for x in range(10):
     print(f'{x+1} {nome}')

# range(valor_inicial, valor_final, incremento)

numero = 1
for x in range(20,2,-2):
    print(x)

pedras = ('Rubi','Esmeralda','Quartzo','Safira','Diamante','Turmalina')

for pedra in pedras:
    if pedra == 'Quartzo':
        continue
    print(pedra)