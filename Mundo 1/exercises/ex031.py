#primeira maneira

print('PROMOÇÃO! Até 200Km/h a viagem possui desconto de R$0,05')
num = float(input('Qual o tamanho da viagem que quer percorrer? ->'))
if num <= 200:
    print('Sua viagem de {}Km/h no total irá custar com desconto, R${}'.format(num,num*0.45))
else:
    print('Sua viagem de {}Km/h no total irá custar sem desconto, R${}'.format(num,num*0.5))

#segunda maneira

print('PROMOÇÃO! Até 200Km/h a viagem possui desconto de R$0,05')
num = float(input('Qual o tamanho da viagem que quer percorrer? ->'))
price = num*0.45 if num <= 200 else num*0.5
print('Sua viagem de {}Km/h no total irá custar R${}'.format(num,price))