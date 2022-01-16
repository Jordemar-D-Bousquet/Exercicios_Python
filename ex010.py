# Crie um programa que mostre quanto dinheiro uma pessoa tem na carteira e quantos dólares ela pode comprar
# considerando U$1,00 = R$3,27

n = float(input('Quando dinhero você tem na carteira? R$ '))

d = n/3.27

print('Com o valor {:.2f}R$ você podera comprar {:.2f}U$ em dolar'.format(n,d))