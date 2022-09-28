# URL do enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761

final = False
valor_compra = 0

while not final:
    price = float(input())
    if(price == 0):
        final = True
    valor_compra += price
    
valor_pago = float(input())
troco = valor_pago - valor_compra

print("Total da compra: R$%.2f" %valor_compra, end='\n')
print("Valor pago: R$%.2f" %valor_pago, end='\n')
print("Troco: R$%.2f" %troco, end='\n')