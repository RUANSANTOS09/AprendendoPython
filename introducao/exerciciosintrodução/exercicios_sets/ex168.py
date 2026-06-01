teams_sp = {'Corinthians','Palmeiras','Santos','São Paulo'}
teams_rj = {'Flamengo', 'Vasco', 'Fluminense', 'São Paulo'}
print(f'Times nos dois estados: {times_sp & times_rj}')
print(f'Times que aparecem só em um dos dois estados {times_sp ^ times_rj}')
print(f'Todos os times {times_sp | times_rj}')
