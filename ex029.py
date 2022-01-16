#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
v = float(input('Qual a velocidade atual do carro: '))
l = 80
m = (v-l)*7
if v > l:
    print('Você foi multado porque excedeu o limite de 80km/h!!')
    print('Sua multa será no valor de {:.2f}'.format(m))
else:
    print('Boa viagem, Dirija com cuidado!!')
