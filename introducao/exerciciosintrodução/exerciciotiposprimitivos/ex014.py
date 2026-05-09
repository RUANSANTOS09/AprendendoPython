preco_produto = float(input('Digite o preço do produto: '))
desconto =float(input('Dono da loja digite o desconto do produto: '))
aplicando_desconto = preco_produto - (preco_produto * desconto)
print('O produto do valor de {} reais será aplicado um desconto de {} %, e será igual a {}'.format(preco_produto, desconto, aplicando_desconto))