# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestacao mensal. Sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.

casa = float(input('Qual eh o valor da casa? R$ '))
salario = float(input('Digite o seu salario: R$ '))
anos = int(input('Quantos anos voce pretende pagar? '))
mensal = casa / (anos * 12)
minimo = salario * 30 / 100
print('Em {} anos, a prestacao mensal vai ficar R${:.2f}!'.format(anos, mensal))
if mensal >= minimo:
    print('Com um salario de R${:.2f}, comprando uma casa de R${:.2f}, em {} anos, a prestacao mensal vai ser R${:.2f}. Emprestimo NEGADO!'.format(salario, casa, anos, mensal))
else:
    print('Emprestimo pode ser CONCEDIDO!')
