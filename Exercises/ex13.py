'Faca um algoritmo de leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.'

s = float(input('Quanto voce ganha? R$'))
a = s * 0.15 + s
print('Com o aumento de 15%, o seu salario que era de R${:.2f} fica agora R${:.2f}!'.format(s, a))
