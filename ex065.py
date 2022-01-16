#Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
cont = 1
soma = maior = menor = 0

n = int(input('Digite um valor: '))
soma = maior = menor = n
resp = str(input('Quer Continuar?[S/N]: ')).upper()
while resp == 'S':
    n = int (input('Digite um valor: '))
    cont += 1
    soma += n
    if n >= maior:
        maior = n
    else:
        menor = n
    resp = str(input('Quer Continuar?[S/N]: ')).upper()
media = soma / cont
print('Você digitou {} números'.format(cont))
print('A média entre os valores é {:.2f}, o maior número é {} e o menor número é {}'.format(media,maior,menor))
