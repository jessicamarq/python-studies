dis = float(input('Qual distância você percorreu em KM? '))
if (dis <= 200):
  valor = dis*0.50
  print(f'O valor da passagem fica R${valor:.2f}')
else:
  valor = dis*0.45
  print(f'Você está prestes a começar uma viagem mais longe, então o valor da passagem fica R${valor:.2f}')