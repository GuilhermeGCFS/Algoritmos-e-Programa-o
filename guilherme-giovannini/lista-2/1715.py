codigo = int(input())
valor_compra = float(input())

comum = valor_compra
funcionario = valor_compra - valor_compra * 0.13
premium = valor_compra - valor_compra * 0.07

if codigo == 1:
    print ("Valor total a ser pago: R$%.2f" %comum, end='\n')
elif codigo == 2:
    print ("Valor total a ser pago: R$%.2f" %funcionario, end='\n')
elif codigo == 3:
    print ("Valor total a ser pago: R$%.2f" %premium, end='\n')
else:
    print ("OPÇÃO INVÁLIDA!", end='\n')