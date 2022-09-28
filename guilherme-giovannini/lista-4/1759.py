# URL do enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

ano_atual = int(input())
salario_base = 1000.00
aumento_base = 0.015
ano_inicial = 2007
if (ano_atual < 2006):
    print("O ano informado deverá ser  2005!", end='\n')
else:
    if (ano_atual == 2006):
        salarioAtual = salario_base + (salario_base * aumento_base)
    else:
        salarioAtual = salario_base + (salario_base * aumento_base)
        for ano_inicial in range(2007, ano_atual + 1):
            aumento_base += 0.010
            salarioAtual = salarioAtual + (salarioAtual * aumento_base)
    print("Salário atual: R$%.2f" %salarioAtual, end='\n')