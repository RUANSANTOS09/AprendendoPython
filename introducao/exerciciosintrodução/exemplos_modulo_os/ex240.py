import os
joining_folders = os.path.join('dados_brutos', 'csv', 'json')
creating_multiple_folders = os.makedirs('dados_brutos/csv/json')
print(os.listdir('dados_brutos'))