#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

maior = 0
menor = 0

for c in range (1,6):
    p = float(input('Qual o peso da {}º pessoa?: '.format(c)))
    if  c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
             menor = p
print('O maior peso lido é de {}kg'.format(maior))
print('O menor peso lido é de {}kg'.format(menor))


