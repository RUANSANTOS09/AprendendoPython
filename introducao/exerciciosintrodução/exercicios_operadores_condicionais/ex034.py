velocidade = float(input('Digite a velocidade KM/h '))
if (velocidade < 40):
    print('Velocidade muito baixa, risco de acidente')
elif(velocidade <= 60):
    print('Velocidade permitida em área urbana')
elif(velocidade <= 80):
    print('Velocidade permitida em via secundária')
elif(velocidade <= 110):
    print('Velocidade permitida em roodovia')
else:
    print('Acima do limite! Multo aplicada.')