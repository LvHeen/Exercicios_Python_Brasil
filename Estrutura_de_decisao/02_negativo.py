'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''

n = float(input('Digite um valor positivo ou negativo: '))

if n < 0:
    print(f'{n} é negativo')
else:
    print(f'{n} é positivo')