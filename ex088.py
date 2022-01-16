#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from time import sleep
from random import randint
print('_='*30)
print('NUMEROS DA MEGA SENA')
print('_='*30)
lista = []
jogos = []
quant = int(input('Quantos jogos você quer que eu sorteie?: '))
cont = 0
tot = 1

while tot <= quant:
    cont = 0
    while True:
        n = randint(1,60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-='* 3, f'SORTEANDO {quant} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}:{l} ')
    sleep(1)
print('-='*5 ,'BOA SORTE','-='*5 )







