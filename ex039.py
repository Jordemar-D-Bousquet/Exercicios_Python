#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

n = int(input('Qual o ano do seu nascimento?: '))
a = 2021 - n
i1 = 18 - a
i2 = a - 18
if a < 18:
    print('Sua idade é {} anos ainda faltam {} anos para você se alistar'.format(a,i1))
elif a > 18:
    print('Sua idade é {}, você deveria ter se alistado há {} anos atrás'.format(a,i2))
elif a == 18:
    print('Você tem {} anos e deve se alistar IMEDIATAMENTE'.format(a))
