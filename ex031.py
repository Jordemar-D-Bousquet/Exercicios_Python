#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

k = float(input('Qua a distancia da sua viagem em Km?: '))
if k < 200:
    v1 = k*0.50
    print('O valor da sua viagem deu {:.2f}R$'.format(v1))
else:
    v2 = k*0.45
    print('O valor promocional da sua viagem deu {:.2f}'.format(v2))
