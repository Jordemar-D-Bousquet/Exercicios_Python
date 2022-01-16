# screva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Qual o valor do salario do funcionáio?: '))
if s <= 1250.00:
    v = (s * 15) / 100
    ns = s + v
    print('Quem recebia {:.2f}R$ tem um aumento de 15% e passa a receber {:.2f}R$'.format(s, ns))
else:
    v = (s * 10) / 100
    ns = s + v
    print('Quem recebia {:.2f}R$ tem um aumento de 10% e passa a receber {:.2f}'.format(s,ns))

