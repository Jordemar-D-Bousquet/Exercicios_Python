#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

lista = []
pessoas = []
maior = menor = 0
opc = ''
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas [1] < menor:
            menor = pessoas[1]
    lista.append(pessoas[:])
    pessoas.clear()
    opc = str(input('Quer continuar: [S/N]: ')).upper().strip()
    if opc == 'N':
        break
    while opc not in 'SN':
        print('Opção inválida')
        opc = str(input('Quer continuar: [S/N]: ')).upper().strip()
        if opc == 'N':
            break
print(f'O total de pessoas cadastradas são: {len(lista)}')
print(f'o maior peso foi de {maior} kg de : ' , end='')
for p in lista:
   if p[1] == maior:
       print(f'{p[0]}',end=' ')
print()
print(f'O menor peso foi de {menor}kg de: ', end='')

for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print()




