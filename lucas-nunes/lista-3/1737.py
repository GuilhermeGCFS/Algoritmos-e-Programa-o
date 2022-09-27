# URL do enunciado

# https://www.beecrowd.com.br/judge/en/custom-problems/view/1737
salarioMinimo = 1192.40
valorHrExtra = 10.00

funcionario = input()
qtdHrExtras = float(input())

salarioBruto = (3 * salarioMinimo) + (valorHrExtra * qtdHrExtras)
salarioLiquido = 0

if salarioBruto < 2000:
    salarioLiquido = salarioBruto - (salarioBruto * 0.05)
elif salarioBruto < 2500 and salarioBruto > 2000:
    salarioLiquido = salarioBruto - (salarioBruto * 0.12)
else:
    inss = salarioBruto * 0.12
    imposto = salarioBruto * 0.20
    salarioLiquido = salarioBruto - (inss + imposto)

print("Nome:", funcionario, end='\n')
print("Salário bruto: R$%.2f" %salarioBruto, end='\n')
print("Salário líquido: R$%.2f" %salarioLiquido, end='\n')