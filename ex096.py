#Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    a = larg*comp
    print(f'A aréa de um terreno {larg}x{comp} é igual a {a}m²')


print('Controle de terrenos')
print('-='*30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)