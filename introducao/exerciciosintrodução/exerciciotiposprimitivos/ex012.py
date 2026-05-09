saldo = float(input('Qual o seu saldo: '))
dolarpreco = 4.92
conversor = saldo/dolarpreco
print('Você tem {} reais, você poderá comprar {:.2f} dolares'.format(saldo, conversor))