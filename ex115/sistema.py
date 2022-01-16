from ex115.lib.interface import *
from ex115.lib.aquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    CriarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta == 1:
       # opção de listar um conteúdo do arquivo.
        LerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema... Até logo')
        break
    else:
        print(f'\033[0;31mERRO! Digite uma Opção Válida !!!\033[m')
    sleep(2)


