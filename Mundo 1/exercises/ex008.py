num = float(input('Uma distâncio em metros: '))
print('A medida {}m corresponde a:'.format(num))
print('{}km'.format(num/1000))
print('{}hm'.format(num/100))
print('{}dam'.format(num/10))
print('{}m'.format(num))
print('{:.0f}dm'.format(num*10))
print('{:.0f}cm'.format(num*100))
print('{:.0f}mm'.format(num*1000))