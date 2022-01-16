# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)


r1 = float(input('Primeiro Seguimento: '))
r2 = float(input('Segundo Seguimento: '))
r3 = float(input('Terceiro Seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os seguimentos acima PODEM FORMAR UM TRIÂNGULO')
else:
    print('os seguimentos acima NÂO PODEM FORMAR UM TRIÂNGULO')
