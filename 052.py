#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
for c in range(1, n+1):
    if n % c ==0:
        print('\033[34m', end =' ')
    else:
        print('\033[31m', end= ' ')
    print(c,end=' ')
