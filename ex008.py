#Escreva um programa que leia o valor em metros e o exiba convertido em milímetros e centímetros

me = float(input(' Digite o valor em metros: '))

ce = me*100
mi = me*1000

print('O valor em centímetros é {} e o valor em milimetros é {}'.format(ce,mi))