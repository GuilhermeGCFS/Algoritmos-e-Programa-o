# URL do enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

valor = float(input())
horas = float(input())
salario = valor * horas
print('Salário bruto: R$%.2f' % salario, end='\n')
ir = (0.11 * salario)
print('Imposto: R$%.2f' % ir, end='\n')
inss = (0.08 * salario)
print('INSS: R$%.2f' % inss, end='\n')
sind = (0.05 * salario)
print('Sindicato: R$%.2f' % sind, end='\n')
desc = ir + inss + sind
salarioL = salario - desc
print('Líquido: R$%.2f' % salarioL, end='\n')
