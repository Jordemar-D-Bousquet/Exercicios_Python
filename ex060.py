# Faça um programa que leia um número qualquer e mostre o seu fatorial.


from math import factorial
n = int (input('Digite um número para ver o seu fatorial: '))
f = factorial(n)
c = n
print('Calculando {}! '.format(n),end ='')
while c > 0:
    print('{}'.format(c), end ='')
    print(' x ' if c > 1 else ' = ', end = '')
    c -= 1
print('{}'.format(f))


