#: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.


lista = []
num = 0
opc = ''
while True:
    lista.append(int(input('Digite um valor: ')))
    num += 1
    opc = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while opc not in 'SN':
            print('Opção inválida.')
            opc = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if opc in 'N':
            break


print('-='*30)
print(f'Você digitou {num} elementos')
print(f'Os valores ordenados de forma decrescente são {sorted(lista, reverse = True)}')
if 5 in lista:
    print('O numéro 5 está na lista')
else:
    print('O número 5 não está na lista')


