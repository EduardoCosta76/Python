# Crie um programa que leia uma frase e diga se ela eh um palindromo, desconsiderando os espacos.
'''Ex:
Apos a sopa
a sacada da casa
A torre da derrota'''


f = str(input('Digite uma frase: ')).upper().strip()
palavras = f.split()
junto = ''.join(palavras)
print('Voce digitou a frase {}'.format(junto))
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palindromo')
else:
    print('NAO temos um palindromo!')