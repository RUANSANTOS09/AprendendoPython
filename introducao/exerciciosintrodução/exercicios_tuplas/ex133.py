nomes = ('Ruan','Ruan','THiago','Fernando','Heloisa')
lista = list(nomes)
nomes_reptidos = []
for n in lista:
    if n not in nomes_reptidos:
        nomes_reptidos.append(n)

print(nomes_reptidos)
