# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

a1 = input('Digite o nome do aluno1: ')
a2 = input('Digite o nome do aluno2: ')
a3 = input('Digite o nome do aluno3: ')
a4 = input('Digite o nome do aluno4: ')

lista = [a1,a2,a3,a4]

random.shuffle(lista)

print('A ordem de apresentação será: {}'.format(lista))