# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros


print('{:=^40}'.format(' LOJAS GUANABARA '))
c = float(input('Digite o valor da compra R$ '))
p = int(input('Digite [1] para pagamento à vista com dinheiro/cheque \nDigite [2] para pagamento à vista no cartão'
              '\nDigite [3] para pagamento em até 2x no cartão \nDigite [4] para pagamento em 3x ou mais no cartão'
              '\nDigite a Opção de Pagamento: '))
if p == 1:
    v = (c * 10) / 100
    vf = c - v
    print('Para pagamento à vista com dinheiro ou cheque voce tem 10% de desconto'
          '\nO valor da compra será de {:.2f}R$'.format(vf))
elif p == 2:
    v = (c * 5) / 100
    vf = c - v
    print('Para pagamento à vista no cartao tem 5% de desconto'
          '\nO valor da compra será de {:.2f}R$'.format(vf))
elif p == 3:
    v = c / 2
    print('Parcelado em 2x o valor da parcela será de {:.2f}R$'.format(v))
elif p == 4:
    j = (c * 20) / 100
    jf = c + j
    v = int(input('Digite em quantas vezes será parcelado: '))
    vf = jf / v
    print('Para pagamento em 3x ou mais no cartão ha um juros de 20%'
          '\nO valor total da compra sera de {:.2f}R$ com parcelas no valor de {:.2f}R$'.format(jf, vf))
