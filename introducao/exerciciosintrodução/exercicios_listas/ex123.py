nomes = ['Paulo','Pedro','Juvenal','Leandro','Bernardo','Bernardo']
nomes_repetidos = 0
nome_digitado = str(input('Digite um nome e vejo quantas vezes ele aparece na lista: '))
for nome in nomes:
    if(nome_digitado in nome):
        nomes_repetidos += 1
print(nomes_repetidos)