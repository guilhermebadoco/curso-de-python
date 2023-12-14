num1 = int(input('Digite um número: '))
num2 = int(input('Será multiplicado por: '))
num3 = int(input('Será dividido por: '))
num4 = int(input('Será elevado á: '))
dob = num1*num2
raiz = num1**(1/2)
elev = pow(num1,num4)
div = num1 / num3
print('-A multiplicação de {} por {}, é: {}'.format(num1, num2, dob))
print('-A raiz quadrada de {}, é {}'.format(num1, raiz))
print('-A divisão de {} por {}, é {}'.format(num1, num3, div))
print('-O valor {} elevado á {} é {}'.format(num1, num4, elev))