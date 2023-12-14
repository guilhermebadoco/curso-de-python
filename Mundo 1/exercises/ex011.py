num1 = float(input('Qual a altura em metros? '))
num2 = float(input('Qual o comprimento em metros? '))
área = num1*num2
print('Contando que o local possui {}mx{}m, Área desse local é de {:.2f}m²'.format(num1,num2,área))
num3 = float(input('Quantos litros de tinta você precisa para pintar um metro do local? '))
tinta = área/num3
print('Para pintar esse local todo, você precisará de {}L de tinta'.format(tinta))