# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {'nome': str(input('Nome de Jogaodor: ')) ,
           'partidas': int(input('Quantas Partidas Jogou: ')),
          'gols': [],}



if jogador['partidas'] != 0:
    for i in range(0,jogador['partidas']):
      jogador['gols'].append((int(input(f'Quantos gols na partida {i+1}: '))))
    jogador['total'] = sum(jogador['gols'])
print('=='*30)
print(jogador)
print('=='*30)
for k , v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for c in range(0, jogador['partidas']):
    print(f'==> Na partida {c+1} fez {jogador["gols"][c]} Gols')
print(f' Total : {jogador["total"]} Gols')

