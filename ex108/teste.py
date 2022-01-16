from ex108 import moeda

p = float(input('Digite o preço R$:'))
print(f'A medade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando a taxa em 10% de {moeda.moeda(p)} temos {moeda.moeda(moeda.aumentar(p,10))}')