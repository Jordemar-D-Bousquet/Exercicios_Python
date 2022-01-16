#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ('Flamengo', 'Santos' , 'Palmeiras' , 'Gremio' , ' Athlético PR' , 'São Paulo' ,'Internacional',
         'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco de Gama', 'Athlético MG', 'Fluminense', 'Botafogo',
         'Ceará','Cruzeiro','CSA', 'Chapecoense','Avai' )
print('-='*20)
print(f'Lista de times{times}')
print('-='*20)
print(f'Os primeiros 5 colocados {times[0:5]}')
print('-='*20)
print('Os 4 ultimos colocados {}'.format(times[-4:]))
print('-='*20)
print('Times em Ordem Alfabetica{}'.format(sorted(times)))
print('-='*20)
print('O time da Chapecoense está na posição {}'.format(times.index('Chapecoense')+1))
print('-='*20)




