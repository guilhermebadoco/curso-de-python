city = str(input('Digite uma cidade: ')).strip()
print('Sua cidade começa com Santo? ')
print(city[:5].upper() == 'SANTO')
print('Sua cidade começa com Santa? ')
print(city[:5].upper() == 'SANTA')
print('Sua cidade começa com São? ')
print(city[:3].upper() == 'SÃO')