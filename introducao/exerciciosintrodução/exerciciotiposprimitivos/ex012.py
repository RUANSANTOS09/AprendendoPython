saldo = float(input('Quanto dinheiro você tem na carteira? R$'))
dolarpreco = saldo/4.92
europreco = saldo/5.80
print('Com {:.2f}, você pode comprar US${:.2f}'.format(saldo,dolarpreco))
print('Com {:.2f} você pode comprar EU€{:.2f}'.format(saldo,europreco))