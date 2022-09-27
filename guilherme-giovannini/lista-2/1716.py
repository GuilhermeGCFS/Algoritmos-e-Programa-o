plano = input()
salario = float(input())

A = salario + salario * 0.10
B = salario + salario * 0.15
C = salario + salario * 0.20

if plano == 'A':
    print ("Novo salário: R$%.2f" %A, end='\n')
elif plano == 'B':
    print ("Novo salário: R$%.2f" %B, end='\n')
elif plano == 'C':
    print ("Novo salário: R$%.2f" %C, end='\n')