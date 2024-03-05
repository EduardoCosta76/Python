# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de pagamento:
'''- A vista dinheiro/cheque: 10% de desconto
- A vista no cartao: 5% de desconto
- em ate 2x no cartao: preco normal
- 3x ou mais no cartao: 20% de juros'''

produto = float(input('Digite o valor do produto: R$ '))
print('''ESCOLHA A FORMA DE PAGAMENTO ESCOLHENDO AS OPCOES ABAIXO:
1 - A vista dinheiro/cheque
2 - A vista no cartao
3 - em ate 2x no cartao
4 - 3x ou mais no cartao''')
pgto = int(input('Qual vai ser a forma de pagamento? '))
if pgto == 1:
    pgto = produto - (produto * 0.1)
    print('Um produto que custava R${:.2f}, com 10% de desconto, agora vai ficar R${:.2f}!'.format(produto, pgto))
elif pgto == 2:
    pgto = produto - (produto * 0.05)
    print('Um produto que custava R${:.2f}, com 5% de desconto, agora vai ficar R${:.2f}!'.format(produto, pgto))
elif pgto == 3:
    parcela = produto / 2
    print('Preco normal! Parcelado vai ficar R${:.2f} em 2x'.format(parcela))
elif pgto == 4:
    pgto = produto + (produto * 0.2)
    totalparc = int(input('Quantas parcelas? '))
    parcela = produto / totalparc
    print('Sua compra sera parceladas em {}x de R${:.2f} com JUROS'.format(totalparc, parcela))
    print('Um produto que custava R${:.2f}, com 20% de juros, agora vai ficar R${:.2f}!'.format(produto, pgto))
else:
    print('Opcao invalida! Escolha novamente!')