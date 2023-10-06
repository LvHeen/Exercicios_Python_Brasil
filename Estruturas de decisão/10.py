a = input('Qual o seu nome? ')
turno = input('Em qual turno você estuda (M - Matutino, V - Vespertino, N - Noturno) ').upper()
if turno == 'M':
    print(f'Bom dia, {a}!')
elif turno == 'V':
    print(f'Boa tarde, {a}!')
elif turno == 'N':
    print(f'Boa noite, {a}!')