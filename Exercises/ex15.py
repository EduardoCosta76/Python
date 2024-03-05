'Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.'
d = int(input('Digite quantos dias: '))
km = float(input('Digite quantos KM: '))
t = d * 60
p = km * 0.15
r = t + p
print('Em {} dia(s), num percurso total de {}KM, voce vai ter que pagar R${:.2f}!'.format(d, km, r))
