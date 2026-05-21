nome_jogadores = []
placar_jogadores = []
while True:
    nome_jogador = str(input('Digite o nome do jogador: '))
    nome_jogadores.append(nome_jogador)
    pontuacao_jogador = int(input('Digite a pontuação do jogador: '))
    placar_jogadores.append(pontuacao_jogador)
    finalizar = str(input('Finalizar? s/n '))
    if(finalizar == 's' or finalizar == 'S'):
        break
placar_jogadores.sort()
nome_jogadores.sort()
print(nome_jogadores)
print(placar_jogadores)
