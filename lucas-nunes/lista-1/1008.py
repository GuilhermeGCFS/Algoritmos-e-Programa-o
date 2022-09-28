# URL do enunciado

# https://www.beecrowd.com.br/judge/en/custom-problems/view/1008
numero = int(input())
horasTrabalhadas = int(input())
valorHora = float(input())
salario = horasTrabalhadas * valorHora
print("NUMBER =", numero, end='\n')
print("SALARY = U$ %.2f" %salario, end='\n')