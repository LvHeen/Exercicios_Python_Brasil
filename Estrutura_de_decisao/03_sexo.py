'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

s = input('Informe seu sexo [M / F]: ').upper()
if s == 'M':
    print('Sexo masculino.')
elif s == 'F':
    print('Sexo feminino.')
else:
    print('Sexo inválido.')
