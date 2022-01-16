#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Quantos dias o carro foi alugado? : '))
k = float(input(' Quantos Km rodados? : '))

vd = d*60
vk = k*0.15

t = vd + vk

print('O total a ser pago é {:.2f}'.format(t))

