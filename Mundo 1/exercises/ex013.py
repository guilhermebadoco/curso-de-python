num1 = (float(input('Qual o salário do funcionário: ')))
num2 = (float(input('Qual o aumento que ele recebe: ')))
SaFi = num1+(num1*num2/100)
print('Contando que o funcionário recebe {}, e que ele possui {:.2f}%, de aumento, o salário final dele é de {}R$'.format(num1,num2,SaFi))