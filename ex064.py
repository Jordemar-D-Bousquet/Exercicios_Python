#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag



tot = 0
cont = 1
n = 0
while n != 999:
    n = int(input('Digite um número inteiro [999 para parar]: '))
    cont += 1
    tot += n
cont -= 1
tot -= 999
print('Você digitou {} números e a soma entre eles é {}'.format(cont,tot))






