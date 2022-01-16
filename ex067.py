# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Digite um número para ver a sua tabuada ou um número negativo para parar: '))
    if n < 0:
        break
    print('='*30)
    for c in range(1,11):
        m = n*c
        print(f'{n} x {c} = {m}')
    print('=' * 30)
print('Fim da Tabuada!!!')