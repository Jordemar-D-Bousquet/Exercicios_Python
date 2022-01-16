# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
s = nome.split()

print('Muito prazer em te conhecer!!')
print('Seu primento nome é {}'.format(s[0]))
print('Seu ultimo nome é {}'.format(s[len(s)-1]))