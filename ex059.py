#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa


sair = False
while not sair:
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))

    op = int(input('''Digite a opção para utilizacão dos valores:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
: '''))
    if op == 1:
        s = v1 + v2
        print('A soma entre {} e {} é igual a {}'.format(v1,v2,s))
    if op == 2:
        m = v1 * v2
        print('A multiplicação entre {} e {} é igual a {}'.format(v1,v2,m))
    if op == 3:
        if v1 > v2:
            print('Entre os valors {} e {} o maior é {}'.format(v1,v2,v1))
        else:
            print('Entre os valors {} e {} o maior é {}'.format(v1,v2,v2))
    if op == 4:
        print('Digite novos valores')
    if op == 5:
        sair = True
print('Saindo do Programa')





