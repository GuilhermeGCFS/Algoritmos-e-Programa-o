# URL do enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = input()
hr_ext_trab = float(input())

salario_min = 1192.40
val_hr_ext = 10.00

salario_hr_ext_trab = hr_ext_trab * val_hr_ext
salario_bruto = 3 * salario_min + salario_hr_ext_trab

if salario_bruto > 2.000:
    dscnt_inss = 0.12 * salario_bruto
else:
    dscnt_inss = 0.05 * salario_bruto

if salario_bruto > 2.500:
    dscnt_ipr = 0.20 * salario_bruto
else:
    dscnt_ipr = salario_bruto
    
descontos = dscnt_inss + dscnt_ipr
salario_liquido = salario_bruto - descontos

print("Nome: %s" %(nome))
print("Salário bruto: R$%.2f" %salario_bruto, end='\n')
print("Salário líquido: R$%.2f" %salario_liquido, end='\n')