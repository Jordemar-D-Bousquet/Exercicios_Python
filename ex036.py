#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

c = float(input('Qual o valor da casa?: '))
s = float(input('Qual o salário do comprador?: '))
a = int(input('Em quantos anos pretende pagar?: '))

vp = c / (a * 12)
ps = s*30 / 100

if vp <= ps:
    print('O valor da casa é {:.2f}R$ é a prestação ficaria {:.2f}R$, Emprestimo NEGADO!!'.format(c,vp))
else:
    print('O valor da casa é {:.2f}R$ e a prestação ficaria {:.2f}R$, Emprestimo CONCEDIDO!!'.format(c,vp))