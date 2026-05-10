largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura*altura
tinta_necessaria = area/2
print('Sua parede tem a dimensão de {} x {} e sua área é de {:.2f}m\u00B2.'.format(largura,altura,area))
print('Para pintar essa parede, você precisará de {:.2f}L de tinta.'.format(tinta_necessaria))