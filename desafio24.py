# c = input('Digite o nome de uma cidade: ').lower().strip()  
# print(c[:5] == 'santo')

#outra versão:
c = input('Digite o nome de uma cidade: ').lower().strip()
print(f'{c.startswith('santo')}')