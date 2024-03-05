# Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher a base de conversao:
'''1 para binario
2 para octal
3 para decimal'''

num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para DECIMAL''')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print('{} convertido para BINARIO eh igual {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAl eh igual {}'.format(num, oct(num)[2:]))
elif opcao ==3:
    print('{} convertido para HEXADECIMAL eh igual {}'.format(num, hex(num)[2:]))
else:
    print('Opcao errada! Tente de novo!')