preco_produto = float(input('Qual é o preço do produto? R$'))
desconto =float(input('Dono da loja digite o desconto do produto: '))
aplicando_desconto = preco_produto - (preco_produto * desconto)
print('O produto que custava {:.2f}, na promoção com desconto de {:.2f}% vai custar R${:.2f}'.format(preco_produto, desconto, aplicando_desconto))