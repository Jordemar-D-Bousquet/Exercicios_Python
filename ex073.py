# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


ex = ('Zero','Um','Dois','Tres','Quatro','Cinco',
      'Seis','Sete','Oito','Nove','Dez','Onze','Doze'
      ,'Treze','Quatorze','Quinze','Dezesseis','Dezessete',
      'Dezoito','Dezenove','Vinte')


num = int(input('Digite um número entre 0 e 20: '))
while num not in range(0,21):
    print('Tente Novamente')
    num = int(input('Digite um número entre 0 e 20: '))
    print(f'Você Digitou o Número: {ex[num]}')


