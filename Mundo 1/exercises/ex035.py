print('\33[1;34m-=-'*20)
print('\33[1;36mEscolha 3 Segmentos Para 1 Triângulo')
print('\33[1;34m-=-'*20)
num1 = float(input('\33[4;37mEscolha o primeiro segmento: '))
num2 = float(input('\33[4mEscolha o segundo segmento: '))
num3 = float(input('\33[4mEscolha o terceiro segmento: '))
if num1<num2+num3 and num2<num1+num3 and num3<num1+num2:
    print('\33[;mOs segmentos que você escolheu \33[32mFORMAM um TRIÂNGULO!')
else:
    print('\33[mOs segmentos que você escolheu \33[31mNÃO FORMAM um TRIÂNGULO!')