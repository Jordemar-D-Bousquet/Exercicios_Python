# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

p = float(input('Digite seu peso atual/kg: '))
a = float(input('Digite sua altura: ' ))

imc = p/(a * a)

if imc < 18.5:
    print('seu IMC é de {:.1f}. Você está abaixo do peso ideal'.format(imc))
elif imc < 25:
    print('Seu IMC é de {:.1f}. Peso Ideal'.format(imc))
elif imc < 30:
    print('seu IMC é de {:.1f}. Sobrepeso'.format(imc))
elif imc < 40:
    print('seu IMC é de {:.1f}. Obesidade'.format(imc))
else:
    print('seu IMC é de {:.1f}. Obesidade Morbida, CUIDADO!!!'.format(imc))


