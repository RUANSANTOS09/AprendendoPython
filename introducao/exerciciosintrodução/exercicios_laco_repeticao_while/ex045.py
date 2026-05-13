contador = 1
soma_total = 0
while(contador <= 5):
    compra = float(input('Digite os valores de cada um dos 5 produtos: R$'))
    contador += 1
    soma_total += compra

print(f'Valor total da compra foi R${soma_total:.2f}')