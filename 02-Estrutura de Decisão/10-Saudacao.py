'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

msg = input('Em qual turno você estuda? (M-matutino, V-verpertino, N-noturno)').upper()

if msg == 'M':
    print('Bom dia!')
elif msg == 'V':
    print('Boa tarde!')
else:
    print('Valor inválido.')