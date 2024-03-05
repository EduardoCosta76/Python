frase = 'Curso em Video Python'

'Comeca da casa 0'

'Fatiamento'
frase[9:13] - 'Comeca na casa 9 e vai ate a 12'
frase[9:21] - 'Comeca na casa 9 e vai ate a 20'
frase[9:21:2] - 'Comeca na casa 9, vai ate a 20, pulando duas casas'
frase[:9] - 'Comeca na casa 0 e vai ate a 8'
frase[9:] - 'Comeca na casa 9 e vai ate a ultima'
frase[9::3] - 'Comeca na casa 9, vai ate a ultima casa, pulando 3 casas'

'Analise'
len(frase) - 'Comprimento da frase'
frase.count('o') - 'Conta quantos o minuscula na frase'
frase.count('o', 0, 13) - 'Frase com fatiamento. Ele vai considerar do 0 ate o 12 e contar quantos o aparecem.'
frase.find('deo') - 'Quantas vezes ele encontrou o deo'
frase.find('Android') - 'Se nao existe a string, ele retorna -1.'
'Curso' in frase - 'Dentro da frase, existe a palavra curso? Ele vai retornar True'

'Transformacao'
frase.replace('Python', 'Android') - 'Troca Python por Android'
frase.upper() - 'Todas as palavras em maiusculas'
frase.lower() - 'Todas as palavras em minusculas'
frase.capitalize() - 'Ele vai pegar a string inteira e transforma em minusculas, e vai deixar so a primeira letra da string em maiuscula'
frase.title() - 'Ele vai transformar a primeira letra de cada palavra em maiusculo'
'  Aprenda Python  ' - frase.strip() - 'Ele vai remover espacos no comeco e no inicio da string'
frase.rstrip() - 'Ele vai remover somente os ultimos espacos'
frase.lstrip() - 'Ele vai remover somente os espacos do comeco'

'Divisao'
frase.split() - 'Ele vai criar uma divisao em cada espaco da string, ele coloca cada palavra dentro de uma lista, onde cada elemento eh separado pelo split'
'-'.join(frase) - 'Vai juntar todos elementos de frase e vai usar o - entre cada palavra'

