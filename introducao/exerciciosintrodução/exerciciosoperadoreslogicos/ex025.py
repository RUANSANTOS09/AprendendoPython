dia_semana = int(input('Qual o dia da semana? '))
verificador = (dia_semana == 6) or (dia_semana == 7)
print('É final de semana? {}'.format(verificador))