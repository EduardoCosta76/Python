'Faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m2.'

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensao de {} x {} e sua area eh de {}m2. '.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, voce precisa de {} litros de tinta'.format(tinta))