frase = input('Digite uma frase: ').lower().strip()
print(f'A letra \'a\' aparece {frase.count('a')} vezes')
print(f'Ela aparece pela primeira vez na posição {frase.find('a')+1}')
print(f'Ela aparece pela última vez na posição {frase.rfind('a')+1-frase.count(' ')}')