# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

menor = 0
maior = 0

valores = []
for v in range(0,5):
    valores.append(int(input(f'Digite o {v} valor: ')))
    '''if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'Você Digitou os Valores: {valores}')
print(f'O Maior Valor Digitado foi {maior} nas posições' ,end=' ')
for i, c in enumerate(valores):
    if c == maior:
        print(f'{i}...', end='')
print()
print(f'O Menor Valor Digitado foi {menor} nas posições',end=' ')
for i, c in enumerate(valores):
    if c == menor:
        print(f'{i}...', end=' ')
print()'''





print(f'O maior valor é o número {max(valores)} na posição {valores.index(max(valores))}')
print(f'O menor valor é o número {min(valores)} na posição {valores.index(min(valores))}')


