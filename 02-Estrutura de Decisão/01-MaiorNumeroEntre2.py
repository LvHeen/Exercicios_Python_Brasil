'''Faça um Programa que peça dois números e imprima o maior deles.'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('Entre {} e {} o maoir é o {}.' .format(num1, num2, num1))
if num1 < num2:
    print('Entre {} e {} o maoir é {}.' .format(num1, num2, num2))