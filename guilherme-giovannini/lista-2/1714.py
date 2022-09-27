compra = float(input())
lucro1 = compra * 1.45
lucro2 = compra * 1.3
if compra < 20:
    print ("Valor de venda: R$%.2f" %lucro1, end='\n')
else:
    print ("Valor de venda: R$%.2f" %lucro2, end='\n')