# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('='*40)
print('10 TERMOS DA PROGRESSÃO ARITIMÉTICA')
print('='*40)

p = int(input('Primeiro termo: '))
r = int (input('Razão: '))
t = p
cont = 1
while cont <= 10:
    t += r
    cont += 1
    print(t , end=' --> ')
print('FIM')
