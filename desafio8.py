num = float(input('Digite um número em metros para ser convertido: '))
cm = num*100
mm = num*1000
print(f'O número que você digitou equivale a {cm:.0f}cm', end=' ')
print(f'e a {mm:.0f}mm')