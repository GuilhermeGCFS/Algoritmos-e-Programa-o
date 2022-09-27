codigo = int(input())
valorCompra = float(input())

if codigo == 1:
    print("Valor total a ser pago: R$%.2f" %valorCompra, end='\n')
elif codigo == 2:
    valorCompra -= valorCompra * 0.13
    print("Valor total a ser pago: R$%.2f" %valorCompra, end='\n')
elif codigo == 3:
    valorCompra -= valorCompra * 0.07
    print("Valor total a ser pago: R$%.2f" %valorCompra, end='\n')
else:
    print("OPÇÃO INVÁLIDA!", end='\n')