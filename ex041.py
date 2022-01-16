# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date
n = int(input('Digite o ano de nascimento: ').strip())
a = date.today().year - n

if a <= 9:
    print('Você tem {} anos e sua categoria é MIRIM'.format(a))
elif a >= 10 and a <= 14:
    print('Você tem {} anos e sua categoria é INFANTIL'.format(a))
elif a >= 15 and a <= 19:
    print('Você tem {} anos e sua categoria é JÙNIOR'.format(a))
elif a >= 16 and a <= 25:
    print('Você tem {} anos e sua categoria é SÊNIOR'.format(a))
else:
    print('Você tem {} anos e sua categoria é MASTER'.format(a))

