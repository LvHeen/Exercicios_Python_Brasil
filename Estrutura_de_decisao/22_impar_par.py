'''Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).'''

n = int(input('Digite um número inteiro: '))
if (n % 2) == 0:
    print('Esse número é par.')
else:
    print('Esse número é impar.')