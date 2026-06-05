def create_player(username,level):
    return {'username':username,'level':level}
def add_score(player,score):
    player['score'] = score
    return player

user = create_player('Ruan',1)
user_with_score = add_score(user,5)
print(user_with_score)