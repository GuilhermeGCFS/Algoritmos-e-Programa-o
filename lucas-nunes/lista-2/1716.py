# URL do enunciado

# https://www.beecrowd.com.br/judge/en/custom-problems/view/1716
planoTrabalho = input()
salarioAtual = float(input())

if planoTrabalho == 'A':
    salarioAtual += salarioAtual * 0.10
    print("Novo salário: R$%.2f" %salarioAtual, end='\n')
elif planoTrabalho == 'B':
    salarioAtual += salarioAtual * 0.15
    print("Novo salário: R$%.2f" %salarioAtual, end='\n')
elif planoTrabalho == 'C':
    salarioAtual += salarioAtual * 0.20
    print("Novo salário: R$%.2f" %salarioAtual, end='\n')