#faça um algorítimo que leia o preço de um produto e mostre esse produto com 5% de desconto

p = float(input('Digite o preço do produto R$ '))
d = (p*5)/100
f = p - d

print('O preço do produto é R${:.2f} e com 5% de desconto fica R${:.2f}'. format(p,f))