entrada = []
for x in range(5):
    inteiro = int(input())
    entrada.append(int(inteiro))

pares = 0
for y in range(5):
    if entrada[y] % 2 == 0:
        pares += 1
print(pares, "valores pares")