# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
print('{:=^40}'.format(' JOKENPO '))
j = int(input('Suas opções: \n[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura\nQual a sua jogada?: '))
c = randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
if j == 0 and c == 0:
    print('Você escolheu Pedra e o Computador Pedra. Empate')
elif j == 0 and c == 1:
    print('Você escolheu Pedra e o Computador Papel. Você Perdeu')
elif j == 0 and c ==2:
    print('Você escolheu Pedra e o Computador Tesoura. Você Ganhou')
elif j == 1 and c == 0:
    print('Você escolheu Papel e o Computador Pedra. Você Ganhou')
elif j == 1 and c == 1:
    print('Você escolheu Papel e o Computador Papel. Empate')
elif j == 1 and c == 2:
    print('Você escolheu Papel e o Computador Tesoura. Você Perdeu')
elif j == 2 and c == 0:
    print('Você escolheu Tesoura e o Computador Pedra. Você Perdeu')
elif j == 2 and c == 1:
    print('Você escolheu Tesoura e o Computador Papel. Você Ganhou')
elif j == 2 and c == 2:
    print('Você escolheu Tesoura e o Computador Tesoura . Empate')


