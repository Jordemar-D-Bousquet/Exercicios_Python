# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint




def sorteia(valor):
    for c in range(0,5):
        n = randint(0, 10)
        v.append(n)
        if n % 2 == 0:
            p.append(n)
    print(f'Sorteando os {c+1} valores da lista: ', end= '')

def somaPar(par):
    soma.append(sum(par))






#Programa Principal
v= []
p = []
soma = []
sorteia(v)
print(v)
somaPar(p)
print(f'A somando os valores pares de {v} temos : {soma}')




