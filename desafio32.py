ano = int(input('Digite um ano para saber se é bissexto: '))
if (ano % 4 == 0):
  print(f'O ano de {ano} é bissexto')
else:
  print(f'Ano de {ano} não é bissexto.')