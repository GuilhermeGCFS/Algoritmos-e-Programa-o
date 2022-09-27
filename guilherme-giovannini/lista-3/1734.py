# URL do enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

numero = int(input() )

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1
    
print("%i! =" %numero, resultado, end='\n')