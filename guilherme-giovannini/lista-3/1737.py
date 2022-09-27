# URL do enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

quantidade_numeros = int(input())
total = 0

if quantidade_numeros > 0:
    while quantidade_numeros > 0:
        numeros_inseridos = float(input())
        total += numeros_inseridos
        quantidade_numeros -= 1
    print("Soma dos números informados: %.2f" %total, end='\n')
else:
    print("Informe uma quantidade > 0!", end='\n')