# Faça um agorítimo que leia o salário de um funcionário e mostre esse salário com 15% de aumento

s = float(input('Qual o salário do funcionário? R$ '))
ns = s+(s*15/100)

print('O salario {:.2f}R$ com aumento de 15% ficará {:.2f}R$'.format(s,ns))