# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('-=-' *20)
print('Vou pensar em um número de 0 a 5, tente adivindar')
print('-=-'*20)
sleep(2)
n = int(input('em que número eu pensei? : ')) # o jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
s = randint(0, 5) # faz o computador pensar
if n == s:
   print('PARABÉNS, você conseguiu me vencer')
else:
    print('GANHEI, eu pensei no número {} e não no número {}'.format(s,n))


