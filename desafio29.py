v = float(input('Qual a velocidade atual do carro? '))
if (v <= 80):
  print('Tenha um bom dia! Dirija com segurança!')
else:
  print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
  print(f'Você deve pagar uma multa no valor de R${(v-80)*7:.2f}')
  print('Tenha um bom dia e dirija com segurança!')