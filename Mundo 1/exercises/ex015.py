num1 = (float(input('Por quantos dias o carro foi alugado: ')))
num2 = (float(input('Quantos quilômetros ele percorreu: ')))
num3 = (float(input('Qual o preço do aluguel por dia? ')))
num4 = (float(input('Qual o preço do aluguel por KM? ')))
pagar = (num1*num3) + (num2*num4)
print('Contando que o carro foi alugado por {} dias que custa {}R$ por dia, e andou {}KM que custa {}R$ por KM'.format(num1,num3,num2,num4))
print('O preço final a pagar é de: {}R$'.format(pagar))