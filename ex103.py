#Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>',gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')




#Programa Principal
n = str(input('Nome do Jogador: '))
g = str(input('Numero de Gols: '))
if g.isnumeric():
    g = int(g)
else:
   g = 0
if n.strip() == '':
    ficha(gols = g)
else:
    ficha(n,g)
