#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite a temperatura em ºC: '))

f = ((9*c)/5)+32

print('A temperarura em {}ºC ficara {}ºF'.format(c,f))