import math
livros1 = ['O poder do Hábito', 'Habitos Atômicos', 'Pense e Enriqueça', 'O Homem mais rico da Babilônia']
quantidades_paginas_livros1 = [408, 320, 368, 160]

livros2 = ['Os 7 Hábitos das Pessoas Altamente Eficazes', 'O Milagre do Amanhã', 'A Coragem de Ser Imperfeito', 'Mindset: A Nova Psicologia do Sucesso']
quantidades_paginas_livros2 = [462, 196, 208, 312]

prateleira1 = ['Essencialismo', 'A Unica Coisa', 'Rápido e Devagar']
quantidades_paginas_livros_pratileira1 = [272, 240, 624]

paginas = quantidades_paginas_livros1 + quantidades_paginas_livros2 + quantidades_paginas_livros_pratileira1
livro_mais_longo = max(paginas)
livro_mais_curto = min(paginas)
media_paginas = sum(paginas) / len(paginas)
result_media = math.trunc(media_paginas)
lista_ordenada = sorted(paginas)

prateleiras = livros1 + livros2 + prateleira1
quantidade_de_livros = len(prateleiras)
new_livro = prateleiras.append('Biblia')
removendo_primeiro_livro = prateleira1.pop(0)

print(f'Total de livros: {quantidade_de_livros}\nO livro mais longo tem {livro_mais_longo} paginas\nO livro mais curto tem {livro_mais_curto} paginas\nA média de paginas dos {quantidade_de_livros} é {result_media}\nLista ordenada: {lista_ordenada}')