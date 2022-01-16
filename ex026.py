#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

f = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes'.format(f.count('A')))
print('Ela aparece na primeira vez em {} posição'.format(f.find('A')+1))
print('Ela aparece na ultima vez na posição {}'.format(f.rfind('A')+1))