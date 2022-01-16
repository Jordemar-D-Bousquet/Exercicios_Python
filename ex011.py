#Faça um programa que leia a largura e a altura de uma parede em metros , calcule a sua área e a
# quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²

larg = float(input('Largura da parede : '))
alt = float(input( 'Altura da parede : '))

area = larg * alt

print('Sua parede tem dimensões de {}x{} e sua area é {}m²'.format(larg,alt,area))

tinta = area/2

print('Para pintar esta parede você precisará de {}LT de tinta'.format(tinta))
