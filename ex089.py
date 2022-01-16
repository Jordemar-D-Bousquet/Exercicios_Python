#  Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#  No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
#  de cada aluno individualmente.

ficha = []
opc = ''
while True:
     n = str(input('Nome: '))
     n1 = float(input('Primeira nota: '))
     n2 = float(input('Segunda nota: '))
     mn = (n1+n2)/2
     ficha.append([n,[n1,n2], mn])
     opc = str(input('Quer continuar [S/N]: '))
     if opc in 'Nn':
         break
print('-='*30)
print(f'{"No":<4}{"NOME":<40}{"MEDIA":>8}')
print('-' *26)
for i, a in enumerate(ficha):
     print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
     print('-'*35)
     opc2 = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
     if opc2 == 999:
          print('FINALIZANDO')
          break
     if opc2 <= len(ficha) -1:
          print(f'Notas de {ficha[opc2][0]} são {ficha[opc2][1]}')
print('<<<VOLTE SEMPRE>>>')

