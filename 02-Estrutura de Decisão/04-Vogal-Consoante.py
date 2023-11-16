'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

letra = input('Digite ume letra: ').upper()
vogal = ['A', 'E', 'I', 'O', 'U']

if letra in vogal:
    print(f'A letra {letra} é uma vogal')
else:
    print(f'A letra {letra} é uma consoante')