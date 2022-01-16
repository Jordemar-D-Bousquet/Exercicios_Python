# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print('-='*30)
print('Vamos jogar par ou impar??')
print('-='*30)

cont = 0
while True:
    jog = int(input('Digite um valor de 0 a 10: '))
    comp = randint(0,10)
    tot = jog + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jog} e o Computador jogou {comp}. Total de {tot}', end = ' ')
    print('DEU PAR' if tot % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if tot % 2 == 0:
            cont += 1
            print('Jogador venceu')
        else:
            print('Computador Venceu')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            cont += 1
            print('Jogdor Venceu')
        else:
            print('Computador Venceu')
            break
    print('Vamos jogar novamente...')
print(f'Total de rodadas vencidas pelo jogador: {cont}')

