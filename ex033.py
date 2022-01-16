# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

nt= [n1,n2,n3]

print('O maior número digitado foi {}'.format(max(nt)))
print('O menor número digitado foi {}'.format(min(nt)))