from datetime import date
year = int(input('\33[4mQue ano é Bissexto? Coloque 0 para ver o ano atual -> '))
if year == 0:
    year = date.today().year
if year%4 == 0 and year%100 != 0 or year%400 == 0:
    print('\33[37mO ano {} \33[32mÉ BISSESXTO'.format(year))
else:
    print('\33[37mO ano {} \33[31mNÃO É BISSESXTO'.format(year))