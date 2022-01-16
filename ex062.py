# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('='*40)
print('10 TERMOS DA PROGRESSÃO ARITIMÉTICA')
print('='*40)

p = int(input('Primeiro termo: '))
r = int (input('Razão: '))
t = p
cont = 1
tot = 0
nt = 10
while nt != 0:
    tot = tot + nt
    while cont <= tot:
        t += r
        cont += 1
        print(t , end=' --> ')
    print('PAUSA')
    nt = int(input('Quantos termos deseja mostrar a mais?: '))
print('Progressão finalizada com {} termos no total'.format(tot))

