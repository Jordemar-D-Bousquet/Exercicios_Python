#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


s = str(input('Digite seu sexo [M/F]: ')).upper()[0].strip()
while s not in 'MF':
    s = str(input('Opção inválida, Digite seu sexo[M/F]: ')).upper()[0].strip()
print('Sexo Cadastrado!!')



