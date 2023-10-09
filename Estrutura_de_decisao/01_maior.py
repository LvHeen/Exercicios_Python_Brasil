'''Faça um Programa que peça dois números e imprima o maior deles.'''

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Agora outro número inteiro: '))
maior = n1

if n2 > n1:
    print(f'O maior é {n2}')
else:
    print(f'O maior é {n1}')