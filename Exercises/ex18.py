'Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo'

import math
angulo = float(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Um angulo de {} tem o seu seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(angulo, seno, cosseno, tangente))
