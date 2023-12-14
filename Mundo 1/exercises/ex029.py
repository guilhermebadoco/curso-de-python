player = int(input('Em qual velocidade o carro está: '))
if player <= 90:
    print('Tenha um Bom Dia! Dirija com SEGURANÇA!')
else:
    print('MULTADO! você ecxedeu o Limite permitido de 90Km/h')
    print('Sua multa é de {}R$'.format((player-90)*7))