#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
d = {'Nome': input('Nome: '),
     'Idade': date.today().year - int(input('Ano de nascimento: ')),
     'CTPS': int(input('Carteira de Trabalho(0 se não tiver): '))}


if d['CTPS'] != 0:
    d['contratacao'] = int(input('Ano de contratação: '))
    d['salario'] = float(input('Salário R$: '))
    d['Aposentar'] = int(d['contratacao'] + 35) - (date.today().year - d['Idade'])

print('_='*30)
for v, k in d.items():
    print(f'{v} = {k}')






