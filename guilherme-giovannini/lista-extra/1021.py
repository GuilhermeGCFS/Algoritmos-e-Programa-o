N = float(input())

nota_100 = N // 100
N = N - nota_100*100

nota_50 = N // 50
N = N - nota_50*50

nota_20 = N // 20
N = N - nota_20*20

nota_10 = N // 10
N = N - nota_10*10

nota_5 = N // 5
N = N - nota_5*5

nota_2 = N // 2
N = N - nota_2*2

nota_1 = N // 1
N = N - nota_1*1
nota_1=float('%.2f'% nota_1)
N=float('%.2f'% N)

m50 = N // 0.5
N = N - m50*0.5
m50=float('%.2f'% m50)
N=float('%.2f'% N)

m25 = N // 0.25
N = N - m25*0.25
m25=float('%.2f'% m25)
N=float('%.2f'% N)

m10 = N // 0.10
N = N - m10*0.10
m10=float('%.2f'% m10)
N=float('%.2f'% N)

m5 = N // 0.05
N = N - m5*0.05
m5=float('%.2f'% m5)
N=float('%.2f'% N)

m1 = N * 100
m1=float('%.2f'% m1)
N=float('%.2f'% N)

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(nota_100)))
print('{} nota(s) de R$ 50.00'.format(int(nota_50)))
print('{} nota(s) de R$ 20.00'.format(int(nota_20)))
print('{} nota(s) de R$ 10.00'.format(int(nota_10)))
print('{} nota(s) de R$ 5.00'.format(int(nota_5)))
print('{} nota(s) de R$ 2.00'.format(int(nota_2)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(nota_1)))
print('{} moeda(s) de R$ 0.50'.format(int(m50)))
print('{} moeda(s) de R$ 0.25'.format(int(m25)))
print('{} moeda(s) de R$ 0.10'.format(int(m10)))
print('{} moeda(s) de R$ 0.05'.format(int(m5)))
print('{} moeda(s) de R$ 0.01'.format(int(m1)))