# URL do enunciado

# https://www.beecrowd.com.br/judge/en/custom-problems/view/1009
nome = input()
salario = float(input())
valorVendas = float(input())
salario += valorVendas * 0.15
print("TOTAL = R$ %.2f" %salario, end='\n')