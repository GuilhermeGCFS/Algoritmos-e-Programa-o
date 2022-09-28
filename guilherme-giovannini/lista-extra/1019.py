N = int(input())
hora = N // 60**2
N = N - hora * 60**2

minuto = N // 60
N = N - minuto*60

segundo = N

print('{}:{}:{}'.format(hora, minuto, segundo))