product = ['  Notebook ', 'PC', 'CELULAR', ' Mouse ', 'TV', '  Monitor', 'webcam  ', 'HD']
clear_data = [eletronic.strip().lower() for eletronic in product if len(eletronic.strip()) > 4]
print(clear_data)