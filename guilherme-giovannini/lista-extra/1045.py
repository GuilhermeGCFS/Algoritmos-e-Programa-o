x = input().split()
A, B, C = x

lado1 = float(1)
lado2 = float(1)
lado3 = float(1)
A = float(A)
B = float(B)
C = float(C)

if A >= B and A >= C:
    lado1 = A
    if B >= C:
        lado2 = B
        lado3 = C
    else:
        lado2 = C
        lado3 = B
if B >= A and B >= C:
    lado1 = B
    if A >= C:
        lado2 = A
        lado3 = C
    else:
        lado2 = C
        lado3 = A

if C >= A and C >= B:
    lado1 = C
    if A >= B:
        lado2 = A
        lado3 = B
    else:
        lado2 = B
        lado3 = A             

if A == B and B == C:
    lado1=A
    lado2=B
    lado3=C

A = lado1
B = lado2
C = lado3

if A >= (B + C):
    print('NAO FORMA TRIANGULO')
else:
    if (A ** 2) == (B ** 2 + C ** 2):
        print('TRIANGULO RETANGULO')
    if (A ** 2) > (B ** 2 + C ** 2):
        print('TRIANGULO OBTUSANGULO')
    if (A ** 2) < (B ** 2 + C ** 2):
        print('TRIANGULO ACUTANGULO')
    if (A == B == C):
        print('TRIANGULO EQUILATERO')
    if A == B != C or B == C != A or A == C != B:
        print('TRIANGULO ISOSCELES')