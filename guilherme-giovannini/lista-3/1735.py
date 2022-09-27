# URL do enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1735

contagem_inicial = int(input())
contagem_final = int(input())

while contagem_final <= contagem_inicial:
    print(contagem_inicial, end='\n')
    contagem_inicial -= 1
    
print("Fogo!", end='\n')