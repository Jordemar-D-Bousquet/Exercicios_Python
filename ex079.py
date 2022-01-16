# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Numero já cadastrado, não vou adicionar...')

    opc = str(input('Quer Continuar: [S/N]: ')).upper().strip()
    if opc == 'N':
        break
print(f'Você digitou os valoes {sorted(num)}')
