# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
import time
import random


def ajuda():
    print('\033[7;35m~' * 30)
    print('SISTEMA DE AJUDA PyHELP')
    print('~'* 30)

    while True:
        a = str(input('\033[m \033[1;33m Função ou Blibioteca: \033[m')).lower()
        if a == 'fim':
            print('\033[7;31m ATÉ LOGO \033[m')
            break
        else:
            print('\033[7;30m~'*30)
            print(f'Acessando o manual do comando {a}')
            print('~'*30)
            print('\033[4;46m')
            help(a)


ajuda()
