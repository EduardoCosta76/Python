# Refaca o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
'''- Equilatero: todos os lados iguais
- Isosceles: dois lados iguais
- Escaleno: todos os lados diferentes'''

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulos', end=' ')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES!')
else:
    print('OS SEGMENTOS NAO FORMAM UM TRIANGULO!')