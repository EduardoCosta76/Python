nome = str(input('Qual eh o seu nome? ')).strip()
if nome == 'Eduardo':
    print('Mais que nome lindo voce tem!')
else:
    print('Mais do mesmo, em?')
print('Bom dia, {}'.format(nome))