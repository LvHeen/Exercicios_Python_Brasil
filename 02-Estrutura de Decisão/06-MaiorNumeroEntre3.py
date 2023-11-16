'''Faça um Programa que leia três números e mostre o maior deles.'''

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

maior = n1
if n2 > n1 or n2 > n2:
    maior = n2
if n3 > n1 or n3 > n2:
    maior = n3

print(f'O maior número digitado foi {maior}')