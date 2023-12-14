from random import randint
from time import sleep
comput = randint(1,5) #computador sorteia um número
print('-=-'*20)
print('Vamos jogar um jogo!')
print('Vou pensar em um número de 1 a 5. Tente adivinhar...')
print('-=-'*20)
sleep(5)
print('PENSANDO...')
sleep(3)
player = int(input('E que número eu pensei? -> ')) #player tenta adivinhar
sleep(2)
print('PROCESSANDO...')
sleep(2)
if player == comput:
    print('PARABÉNS! Você GANHOU! Eu também pensei em {}'.format(comput)) #acertou
else:
    print('Que pena! Eu GANHEI! Eu pensei em {} e não em {}!'.format(comput,player)) #errou