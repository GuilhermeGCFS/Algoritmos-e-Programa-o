tempo_viagem = int(input())
velocidade = int(input())
kml = 12
consumo = tempo_viagem * velocidade / kml

print('{:.3f}'.format(consumo))