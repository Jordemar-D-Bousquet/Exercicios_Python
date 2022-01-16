# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
pares = 0
coluna3 = 0
linha2 = []
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posição {l},{c}: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if matriz [l][2]:
            coluna3 += matriz[l][2]
if matriz[1]:
    linha2.append(matriz[1][0])
    linha2.append(matriz[1][1])
    linha2.append(matriz[1][2])
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end= '')
    print()
print('-='*30)
print(f'A soma dos valores pares : {pares}')
print(f'A soma dos valores da 3ª coluna : {coluna3}')
print(f'O maior valor da segunda linha: {max(linha2)}')

