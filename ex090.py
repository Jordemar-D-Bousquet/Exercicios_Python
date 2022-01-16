#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Media do {aluno["nome"]}: '))

if aluno['media'] > 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('_='*30)
for k,v in aluno.items():
    print(f'O {k} é igual a {v}')


