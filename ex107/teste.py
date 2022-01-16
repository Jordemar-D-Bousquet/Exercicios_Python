from ex107 import moeda

p = float(input('Digite o preço R$:'))
print(f'A medade de R${p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é {moeda.dobro(p)}')
print(f'Aumentando a taxa em 10% de {p} temos {moeda.aumentar(p,10)}')