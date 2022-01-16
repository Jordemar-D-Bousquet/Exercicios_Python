#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# para binário, 2 para octal e 3 para hexadecimal.


n = int(input('Escreva um número inteiro: '))
e = int(input('Escolha a base de conversão: \n digite 1 para binário \n digite 2 para octal \n digite 3 para hexadecimal: '))
if e == 1:
    print(bin(n)[2:])
elif e == 2:
    print(oct(n)[2:])
elif e == 3:
    print(hex(n)[2:])
else:
    print('Opção Inválida')