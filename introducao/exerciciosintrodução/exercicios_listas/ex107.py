tempo = [0.43, 0.32, 0.56, 0.45, 0.43, 0.28]
melhor_tempo = min(tempo)
pior_tempo = max(tempo)
ranking = sorted(tempo)
print(f'O melhor tempo da corrida {melhor_tempo}\nO pior tempo da corrida {pior_tempo}\nO ranking final dos melhores tempos {ranking}')