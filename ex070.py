# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.


print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)


menor = cont = mil = totpre = 0
barato = ' '

while True:
    nprod = str(input('Nome do produto: '))
    pre = float(input('Preço R$: '))
    totpre += pre
    cont += 1
    if pre > 1000:
        mil += 1
    if cont == 1:
        barato = nprod
        menor = pre
    else:
        if pre < menor:
            barato = nprod
            menor = pre
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]
    if opc in 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print('O total da compra foi R${:.2f}'.format(totpre))
print(f'{mil} podutos custando mais de R$1000')
print('O produto mais barato foi {} custando R${:.2f}'.format(barato, menor))


