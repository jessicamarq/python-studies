dia = int(input('Digite a quantidade de dias que ficou com o carro: '))
km = float(input('Digite a quantidade de km percorridos: '))
print(f'O valor a pagar é R${(dia*60)+(km*0.15):.2f}')