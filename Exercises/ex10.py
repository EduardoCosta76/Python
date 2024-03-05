'Crie um programa qye leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar'
'Considere: US$1.00 = R$3.27'

d = float(input('Quanto dinheiro voce tem? R$'))
r = d / 3.27
print('Com a cotacao do dolar hoje em dia fixada em US$1.00 = R$3.27, com R${:.2f} voce conseguiria comprar {:.2f} dolares!'.format(d, r))
