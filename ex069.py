# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

mulher20 = 0
hom = 0
pes = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)


    idad = int(input('Idade: '))
    sex = ' '
    opc = ' '
    while sex not in 'MF':
        sex = str(input('Sexo [M/F}: ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Quer continuar?[S/N}: ')).strip().upper()[0]
    if idad >= 18:
        pes += 1
    if sex == 'M':
        hom += 1
    if sex == 'F' and idad <=20:
        mulher20 += 1
    if opc == 'N':
        break
print(f'Voce cadastrou {pes} pessoas com mais de 18 anos')
print(f'Foram cadastrados {hom} pessoas do sexo masculino')
print(f'e {mulher20} mulheres com menos de 20 anos')



