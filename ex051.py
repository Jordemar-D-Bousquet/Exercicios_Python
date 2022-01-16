# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.


print('='*40)
print('10 TERMOS DA PROGRESSÃO ARITIMÉTICA')
print('='*40)

p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
d = p +(10 -1) * r
for c in range(p, d+r, r):
    print(c, end=' --> ')
print('FIM')


