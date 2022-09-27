# URL do enunciado
# https://www.beecrowd.com.br/judge/pt/problems/view/1009

nome = input()
salfixo = float(input())
qtdevendas = float(input())
bonus = float(qtdevendas * (15/100))
total = salfixo + bonus
print(f'TOTAL = R$ {total:.2f}')