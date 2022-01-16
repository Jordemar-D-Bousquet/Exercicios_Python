# Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)

#Adicione também as docstrings dessa função para consulta pelo desenvolvedor.


def notas(*n,sit= False):
    '''
    -> Função para ler várias notas de uma turma de aluno e mostrar os resultados
    :param n: Lê varias notas de alunos
    :param sit: (opcional) mostra a sitação da média de um aluna(Ruim,Razoável ou Boa)
    :return: Quantidade de notas, a maior nota, a menor nota , média e situação(opcional)
    '''
    d = {}
    d['total'] = len(n)
    d['maior'] = max(n)
    d['menor'] = min(n)
    d['media'] = sum(n)/len(n)
    if sit == True:
        if d['media'] < 5:
            d['situação'] = 'Ruim'
        if d['media'] >=5 and d['media'] < 7:
            d['situação'] = 'Razoável'
        if d['media'] >= 7:
            d['situação'] = 'Boa'

    return (d)




#Programa Principal
resp = notas(2.5,2,1,2, sit=True)
print(resp)
#help(notas)