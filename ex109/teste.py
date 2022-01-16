from ex109 import moeda

p = float(input('Digite o preço R$:'))
print(f'A medade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'Aumentando a taxa em 10% de {moeda.moeda(p)} temos {moeda.aumentar(p,10,True)}')
print(f'Dimunuindo o valor de {moeda.moeda(p)} em 13% temos {moeda.diminuir(p,13,True)}')