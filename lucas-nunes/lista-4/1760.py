fim = False;
valorCompra = 0;
while fim != True:
    preco = float(input());
    if (preco == 0):
        fim = True;
    valorCompra += preco;

valorPago = float(input());

troco = valorPago - valorCompra;

print("Total da compra: R$%.2f" %valorCompra, end='\n');
print("Valor pago: R$%.2f" %valorPago, end='\n');
print("Troco: R$%.2f" %troco, end='\n');