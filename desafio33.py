a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
menor = a
if (b<a) and (b<c):
  menor = b
elif(c<a) and (c<b):
  menor = c

maior = a
if (b>a) and (b>c):
  maior = b
elif(c>a) and (c>b):
  maior = c
print(f'O menor número é {menor}')
print(f'O maior número é {maior}')
