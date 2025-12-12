import math
a = float(input('Digite o cateto oposto: '))
b = float(input('Digite o cateto adjacente: '))
c = math.hypot(a, b)
print(f'O valor da hipotenusa é: {c:.2f}')