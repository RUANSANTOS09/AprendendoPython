produtos1 = ['Bola', 'Chuteira', 'Garfo']
preco_produto1 = [76.00, 210.00, 4.00 ]

produtos2 = ['Lapis', 'Borracha', 'Caneta']
preco_produto2 = [3.00, 2.00, 3.00]

produtos3 = ['Lustre', 'Lampada', 'Porta']
preco_produto3 = [400.00, 19.00, 300.00]

preco_produtos = preco_produto1 + preco_produto2 + preco_produto3
produtos = produtos1 + produtos2 + produtos3

print('Total de produtos:',len(produtos))
print(max(preco_produtos))
print(min(preco_produtos))
print(sorted(preco_produtos))

produtos.append('Roteador')
print(produtos)

produtos.pop()
print(produtos)