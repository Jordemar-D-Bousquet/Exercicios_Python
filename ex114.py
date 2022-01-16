#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site do Pudim não está acessível no momento !!')
else:
    print('Consegui acessar o site do pudim !!')
    print(site.read())
    