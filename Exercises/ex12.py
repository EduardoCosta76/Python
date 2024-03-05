'Faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto.'

p = float(input('Quanto custa esse produto? R$'))
d = p - (p * 0.05)
print('O produto custa R${:.2f}, mas com 5% de desconto, fica R${:.2f}'.format(p, d))

