# Refaca o desafio 9, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando laco for.

num = int(input('Digite um numero: '))
for c in range(1, 11):
    print('{} x  {:2} = {}'.format(num, c, num * c))

