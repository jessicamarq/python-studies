salario = float(input('Digite o salário do funcionário: '))
if (salario <= 1250):
  aumento = salario+(salario*0.15)
  print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f}')
else:
  aumento = salario+(salario*0.10)
  print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f}')