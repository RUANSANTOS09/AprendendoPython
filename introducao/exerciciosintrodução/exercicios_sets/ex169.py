programming_languages = {'Python', 'Java','C#', 'Javascript', 'C','C++', 'Cobol', 'Dart', 'Assembly'}
user_language = str(input('Digite sua linguagem e veja se ela está no editor e código: ')).capitalize().strip()
if user_language not in programming_languages:
    print('Sua linguagem não está dentro do editor de código')
else:
    print('Sua linguagem está dentro do editor de código')


