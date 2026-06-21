execution_time = int(input('Digite a quantidade de tempo em segundos: '))
performance = '⚠️ Lento' if execution_time > 300 else '✅ Normal'
print(performance)