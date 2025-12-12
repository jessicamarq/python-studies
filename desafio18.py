import math
ang = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O seno é: {seno:.2f}')
print(f'O cosseno é: {cos:.2f}')
print(f'A tangente é: {tan:.2f}')