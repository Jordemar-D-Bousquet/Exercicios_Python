#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

aluno1 = input('Digite o nome do aluno1 : ')
aluno2 = input('Digiete o nome do aluno2 :')
aluno3 = input('Digite o nome do aluno3: ')
aluno4 = input('Digite o nome do aluno4: ')

sorteado = aluno1,aluno2,aluno3,aluno4

print('O aluno sorteado foi {}'.format(random.choice(sorteado)))
