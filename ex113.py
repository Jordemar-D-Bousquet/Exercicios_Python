# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    valido = False
    while not valido:
        try:
            entrada = int(input(msg))
        except ValueError:
            print(f'\033[0;31mERRO! Digite um número Inteiro !!!\033[m')
        else:
            valido = True
            return entrada


def leiaFloat(msg):
    valido = False
    while not valido:
        try:
            entrada = float(input(msg))
        except ValueError:
            print(f'\033[0;31mERRO! Digite um número Real !!!\033[m')
        else:
            valido = True
            return entrada



i = leiaInt('Digite um valor Inteiro: ')
f = leiaFloat('Digite um valor Real: ')
print(f'O valor interio digitado foi{i} e o valor real digitado foi {f}')

