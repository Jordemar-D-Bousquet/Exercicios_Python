# o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)


r1 = float(input('Primeiro Seguimento: '))
r2 = float(input('Segundo Seguimento: '))
r3 = float(input('Terceiro Seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os seguimentos acima PODEM FORMAR UM TRIÂNGULO', end=' ')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1 :
            print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('os seguimentos acima NÂO PODEM FORMAR UM TRIÂNGULO')