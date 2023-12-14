nome = str(input('Digite uma Frase: ')).strip().upper()
print('-A letra A aparece {} vezes'.format(nome.count('A')+nome.count('Ã')+nome.count('Â')+nome.count('Á')+nome.count('À')+nome.count('Ä')))
print('-A primeira letra A aparece na posição {}'.format(nome.find('A')+1))
print('-A última letra A aparece na posição {}'.format(nome.rfind('A')+1))