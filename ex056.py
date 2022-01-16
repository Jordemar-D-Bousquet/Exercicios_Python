#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


si = 0
mi = 0
mih = 0
nhv =''
tm20 = 0
for c in range(1,5):
    print('---{}ºPessoa ---'.format(c))
    np = str(input('Nome: ')).strip()
    ip = int(input('Idade: '))
    sp = str(input('Sexo [M/F]: ')).strip()
    si += ip
    if c == 1 and sp in 'Mn':
        mih = ip
        nhv = np
    if sp in 'Mm' and ip > mih:
        mih = ip
        nhv = np
    if sp in 'Ff' and ip < 20:
            tm20 += 1

mi = si/4
print('A media de idade do grupo é de {} anos '.format(mi))
print('O homem mais velho se chama {} e tem {} anos '.format(nhv,mih))
print('Ao todo são {} mulheres com menos de 20 anos '.format(tm20))

