sellers = ['Ana', 'Bruno', 'Carlos']
regions = ['Norte', 'Sul', 'Leste']
coverage = [f'{s} - {r}' for s in sellers for r in regions]
print(coverage)