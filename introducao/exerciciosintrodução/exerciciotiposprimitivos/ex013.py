largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura*altura
tinta_necessaria = area/2
print('A area é igual a {} metros quadrados e a quantidade de tinta necessaria sera de {:.2f} litros'.format(area, tinta_necessaria))