valorCompra = float(input())

if valorCompra < 20.00:
    valorCompra += valorCompra * 0.45
    print("Valor de venda: R$%.2f" %valorCompra, end='\n')
else:
    valorCompra += valorCompra * 0.30
    print("Valor de venda: R$%.2f" %valorCompra, end='\n')