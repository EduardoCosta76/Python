# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para salarios superiores a R$1250,00 , calcule um aumento de 10%. Para os inferiores ou iguais, o aumento eh de 15%

salario = float(input('Digite quanto voce ganha: R$ '))
if salario <= 1250:
    aumento = (salario * 0.15) + salario

else:
    aumento = (salario * 0.10) + salario
print('Com um salario de R${:.2f}, o seu salario agora eh de R${:.2f} '.format(salario, aumento))
