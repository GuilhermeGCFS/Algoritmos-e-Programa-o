qtdNumeros = int(input())

contador = 0
total = 0

if qtdNumeros > 0:
    while contador < qtdNumeros:
        total += float(input())
        contador += 1
    print("Soma dos números informados: %.2f" %total, end='\n')
else:
    print("Informe uma quantidade > 0!", end='\n')
