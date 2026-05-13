contador_notas = 1
soma_notas = 0
while(contador_notas <= 4):
    notas = float(input(f'Digite a nota da  {contador_notas}º unidade: '))
    contador_notas += 1
    soma_notas += notas

media_notas = soma_notas / 4
if(media_notas >= 7):
    print(f'Sua média é {media_notas}\nSituação: Aprovado!!!!!!')
elif(media_notas >= 5 and media_notas <= 7):
    print(f'Sua média é {media_notas}\nSituação: Recuperação!!!!')
else:
    print(f'Sua média é {media_notas}\nSituação: Reprovado!!!!!!')