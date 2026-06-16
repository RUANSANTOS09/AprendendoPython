product = ['  Notebook ', 'PC', 'CELULAR', ' Mouse ', 'TV', '  Monitor', 'webcam  ', 'HD']
transitions_usd = [250.0, -30.0, 0, 520.99, -5.0, 89.90, 1200.0, -0.01, 75.0]
sellers = ['Ana', 'Bruno', 'Carlos']
regions = ['Norte', 'Sul', 'Leste']

standardizing_data = [s.lower().strip() for s in product if len(s.strip()) > 4]
transforming_data = [round(conversion * 5.70,2) for conversion in transitions_usd if conversion > 0]
coverage = [f'{s} - {r}' for s in sellers for r in regions]
total_sales = sum(transforming_data)

print(f'Produtos: {standardizing_data}')
print(f'Transações válidas (R$): {transforming_data}')
print(f'Equipes: {coverage}')
print(f'Total de vendas: R$ {total_sales:.2f}')
