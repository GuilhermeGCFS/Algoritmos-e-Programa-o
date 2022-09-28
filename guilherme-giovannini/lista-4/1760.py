# URL do enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

quantidade_pessoas = 0
soma = 0

for x in range(4):
    idade = int(input())
    peso = float(input())
    if(peso > 90):
        quantidade_pessoas += 1;
    soma += idade

media = soma / 4

print("Qtd pessoas > 90 Kg: %i" %quantidade_pessoas, end="\n")
print("Idade média: %.2f" %media, end="\n")