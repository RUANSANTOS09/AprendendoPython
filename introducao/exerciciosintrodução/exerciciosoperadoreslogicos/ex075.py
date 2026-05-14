tem_carteira = True
bebeu = False

if tem_carteira and bebeu :
    print('Você bebeu e não pode dirigir!!')
elif tem_carteira != True and bebeu:
    print('Você está todo errado, primeiro, você bebeu e segundo, você não tem carteira de habilitção')
elif tem_carteira != True and bebeu != True:
    print('Você não tem carteira')
else:
    print('Pode dirigir!')