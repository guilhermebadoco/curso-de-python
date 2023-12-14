num1 = int(input('\33[4mPrimeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro Número: '))
if num1<num2 and num1<num3:
    menor=num1
if num2<num1 and num2<num3:
    menor=num2
if num3<num1 and num3<num2:
    menor=num3
if num1>num2 and num1>num3:
    maior=num1
if num2>num1 and num2>num3:
    maior=num2
if num3>num1 and num3>num2:
    maior=num3
print('\33[mO menor número digitado foi {}'.format(menor))
print('O maior número digitado foi {}'.format(maior))