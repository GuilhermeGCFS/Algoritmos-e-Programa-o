# URL do enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761

final = False
valor_compra = 0

while not final:
    preco = float(input())
    if(preco == 0):
        final = True
    valor_compra += preco
    
valor_pago = float(input())
troco = valor_pago - valor_compra

print("Total da compra:%.2f" %valor_compra, end="\n")
print("Valor pago:%.2f" %valor_pago, end="\n")
print("Troco:%.2f" %troco, end="\n")