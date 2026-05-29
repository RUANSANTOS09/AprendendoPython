greatest_player = ''
highest_score = 0
player_scores = {
    'Pedro': 8,
    'João': 9,
    'Paulo': 7

}
for name,score in player_scores.items():
    print(f'{name}: {score}')
    if score > highest_score:
        highest_score = score
        greatest_player = name
print(f'{greatest_player} tem a maior pontuação com {highest_score} pontos')

for name,score in player_scores.items():
    player_scores[name] = score + 10
    print(f'{name}: {score + 10}')