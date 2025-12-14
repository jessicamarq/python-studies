from random import randint
print('-=-'*15)
print('Tente adivinhar em que número estou pensando...')
print('-=-'*15)
random = randint(0, 5)
n = int(input('Digite um número: '))
if (n == random):
  print(f'Você ganhou! O número que pensei foi {random}!')
else:
  print(f'Você perdeu! Pensei no número {random} e não no {n}')

