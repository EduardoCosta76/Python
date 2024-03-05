nome = str(input('Qual eh o seu nome? '))
if nome == 'Eduardo':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Mario' or nome == 'Paulo':
    print('Seu nome eh bem popular no Brasil')
elif nome in 'Ana Aline Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome eh bem normal')

print('Tenha um bom dia, {}!'.format(nome))