nomes_reptidos = ['Marco','Marco','Carlos','Carlos','Matheus','Matheus']
for nome in nomes_reptidos:
    print(nome)

nomes_sem_repticao = []
for nome in nomes_reptidos:
    if(nome not in nomes_sem_repticao ):
        nomes_sem_repticao.append(nome)

print(nomes_sem_repticao)
