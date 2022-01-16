# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

from random import randint
print('-=-' *20)
print('Vou pensar em um número de 0 a 10, tente adivindar')
print('-=-'*20)
c = randint(0,10)
t = 0
acertou = False
while not acertou:
    j = int(input('Em qual número eu pensei?: '))
    t += 1
    if j == c:
        acertou = True
    if j > c:
            print('Errou, tente um numéro menor.')
    elif j < c:
            print('Errou, Tente um número maior')
print('Acertou!!')
print('Tentativas {}'.format(t))
