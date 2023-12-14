num = float(input('\33[4mQual é o seu salário? R$'))
if num <= 1250:
    print('Seu salário de \33[31mR${} \33[37mrecebe 15% de aumento, que no total fica \33[32mR${}'.format(num,num+(num*15/100)))
else:
    print('Seu salário de \33[31mR${} \33[37mrecebe 10% de aumento, que no total fica \33[32mR${}'.format(num,num+(num*10/100)))