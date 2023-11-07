'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

letra = str(input('Insira uma letra: ')).upper()
if letra == 'A' and 'E' and 'O' and 'O' and 'U':
    print(f'{letra} é vogal')
else:
    print(f'{letra} é consoante')

'''Tentei usar o operador "or" invés de "and", mas não funcionaram e não entendi o porquê'''
