num1 = (float(input('Qual o preço do produto em reais: ')))
num2 = (float(input('Quanto desconto ele possui: ')))
PrFi = num1-(num1*num2/100)
print('O seu produto custando {}R$, com desconto de {}%, fica no preço final: {:.2f}R$'.format(num1,num2,PrFi))