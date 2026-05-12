# Simples, Composto, Aninhado

n1 = n2 = 0.0
media = 0.0
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
# Calculando a média aritmética das notas
media = (n1 + n2) / 2
if (media >= 7):
    print('Sua média é {}\nResultado: Aprovado!!!!'.format(media))
elif (media >= 5):
    print('Sua média é {}\nResultado: Recuperação!!!'.format(media))
else:
    print('Sua média é{}\nResultado: Reprovado!!!!'.format(media))