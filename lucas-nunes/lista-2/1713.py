# URL do enunciado

# https://www.beecrowd.com.br/judge/en/custom-problems/view/1013
valorHora = float(input())
horasTrabalhadas = float(input())

salarioBruto = valorHora * horasTrabalhadas
pgImposto = salarioBruto * 0.11
pgInss = salarioBruto * 0.08
pgSindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - (pgImposto + pgInss + pgSindicato)

print("Salário bruto: R$%.2f" %salarioBruto, end='\n')
print("Imposto: R$%.2f" %pgImposto, end='\n')
print("INSS: R$%.2f" %pgInss, end='\n')
print("Sindicato: R$%.2f" %pgSindicato, end='\n')
print("Líquido: R$%.2f" %salarioLiquido, end='\n')