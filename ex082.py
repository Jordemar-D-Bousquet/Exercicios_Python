# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.


lista = []
pares = []
impares = []
opc = ''
while True :
    n = (int(input('Digite um valor: ')))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    opc = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if opc in 'N':
        break
    while opc not in 'SN':
        print('Opção Inválida')
        opc = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if opc in 'N':
        break
print(f'Os valores Digitados foram {lista}')
print(f'A lista de valores pares são {pares}')
print(f'A lista de valores ímpares são {impares}')