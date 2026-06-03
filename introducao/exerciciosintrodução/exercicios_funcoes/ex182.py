def greeting(name,pd = 'manhã'):
    if pd == 'manhã':
        return f'Bom dia, {name}!'
    elif pd == 'tarde':
        return f'Boa tarde, {name}!'
    else:
        return f'Boa noite, {name}!'
print(greeting('Ruan','tarde'))