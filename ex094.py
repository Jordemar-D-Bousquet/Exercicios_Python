# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

cadastro =[]
pessoas ={}
contidade = 0
mulher = []
acmedia = []
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo[M/F]:'))
    while pessoas['sexo'] not in 'MmFf':
        print('Opção inváçida, Cadastre apenas M ou F')
        pessoas['sexo'] = str(input('Sexo[M/F]:'))
    if pessoas['sexo'] in 'Ff':
        mulher.append(pessoas['nome'])
    pessoas['idade'] = int(input('Idade: '))
    contidade += pessoas['idade']
    cadastro.append(pessoas)
    opc = str(input('Quer continuar?[S/N]: '))
    while opc not in 'SsNn':
        print('Opção Inválida')
        opc = str(input('Quer continuar?[S/N]: '))
    if opc in 'Nn':
        break
media = contidade / len(cadastro)
if pessoas['idade'] > media:
    acmedia.append(pessoas['nome'])
print('-='*30)
print(f'Foram cadastradas {len(cadastro)} pessoas')
print(f'A media de idade entre eles é {media:.1f}')
print(f'A mulheres cadastradas foram {mulher}')
print(f'As pessoas Cadastradas acima da média são {acmedia}')