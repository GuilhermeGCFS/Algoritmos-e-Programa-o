quantidade_pessoas = 0
soma = 0

for x in range(4):
    idade = int(input())
    peso = float(input())
    if(peso > 90):
        quantidade_pessoas += 1;
    soma += idade

print("Qtd pessoas > 90 Kg: %.2f" % quantidade_pessoas, end="\n")
media = soma / 4
print("Idade média: %.2f" % media, end="\n")