valor_compra = float(input('Digite o valor total da compra R$'))
desconto_dez = valor_compra - (valor_compra * 10/100)
desconto_vinte = valor_compra - (valor_compra * 20/100)
desconto_trinta = valor_compra - (valor_compra * 30/100)
if(valor_compra < 100):
    print('Sem desconto')
elif(valor_compra >= 100 and valor_compra <= 299):
    print('Seu produto custou R${:.2f} e será aplicado um desconto de 10%, ele passa a custar R${:.2f}'.format(valor_compra, desconto_dez))
    percentual = 0.10
elif(valor_compra >= 300 and valor_compra <= 499):
    print('Seu produto custou R${:.2f} e será aplicado um desconto de 20% ele passa a custar R${:.2f}'.format(valor_compra,desconto_vinte))
else:
    print('Seu produto custou R${:.2f} e será aplicado um desconto de 30%, ele passa a custar R${:.2f}'.format(valor_compra,desconto_trinta))