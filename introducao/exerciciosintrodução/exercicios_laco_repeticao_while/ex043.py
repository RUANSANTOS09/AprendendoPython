tentativas = 3
senha_correta  = 'python123'
while (True):
    senha = str(input('Digite sua senha:'))
    if(senha == senha_correta):
        print('Senha Correta, Bem vindo a sua conta')
        break
    elif(senha != senha_correta and tentativas >= 1 and tentativas <= 3):
        print(f'Senha incorreta, Você tem mais {tentativas} tentativas.')
        tentativas -= 1
    elif(tentativas == 0):
        print('Você não tem mais tentativas, Conta Bloqueada!!!')
        break






