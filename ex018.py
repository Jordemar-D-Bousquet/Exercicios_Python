#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
an = float(input(' Digite um ângulo que você deseja: '))
sen = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an,sen))
con = math.cos(math.radians(an))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(an,con))
tang = math.tan(math.radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an,tang))