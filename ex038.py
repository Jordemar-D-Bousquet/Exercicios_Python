#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são

n1 = int(input('Escreva o primeiro número: '))
n2 = int(input('Escrea o segundo número: '))
if n1 > n2:
    print('O primeiro valor {} é maior que o segundo {}'.format(n1,n2))
elif n2 > n1:
    print('O segundo valor {} é maior que o primeiro {}'.format(n2,n1))
elif n1 == n2:
    print('Os dois valores são iguais')
else:
    print('Opção inválida, tente novamente')
