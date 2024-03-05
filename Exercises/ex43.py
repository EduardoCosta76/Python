# Desenvolva uma logica que leia o peso e a altura de uma pessoa e calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
'''- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 ate 30: Sobrepeso
- 30 ate 40: Obesidade
- Acima de 40: Obesidade morbida'''

peso = float(input('Digite o seu peso: (Kg)'))
altura = float(input('Digite a sua altura: (m)'))
imc = peso / (altura**2)
if imc < 18.5:
    print('Com um IMC de {:.1f}, voce esta abaixo de 18.5, ou seja, abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Com um IMC de {:.1f}, voce esta com o peso ideal!'.format(imc))
elif imc >=25 and imc < 30:
    print('Com um IMC de {:.1f}, voce esta com sobrepeso!'.format(imc))
elif imc >=30 and imc < 40:
    print('Com um IMC de {:.1f}, voce esta obeso!'.format(imc))
else:
    print('Com um IMC de {:.1f}, voce esta com obesidade morbida!'.format(imc))