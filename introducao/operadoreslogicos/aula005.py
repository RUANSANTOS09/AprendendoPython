# --------------- AND ---------------
idade = int(input('Diga sua idade: '))
altura = float(input('Diga sua altura: '))
resultado = (idade >= 18) and (altura >= 1.70)
print('Pode participar do evento? {}'.format(resultado))
# --------------- OR ---------------
# Programa de disparo de alarme
porta = 'Fechado'
janela = 'Aberta'
alarme = (porta == 'Aberta') or (janela == 'Aberta')
print('Alarme disparado? {} '.format(alarme))
# --------------- NOT ---------------
tem_dinheiro = False
tem_dinheiro = not tem_dinheiro
msg = 'Tem dinheiro? {}'.format(tem_dinheiro)
print(msg)
