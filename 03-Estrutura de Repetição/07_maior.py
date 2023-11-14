'''Faça um programa que leia 5 números e informe o maior número.'''

num = []
for n in range (1, 6):
    num.append(int(input(f'{n}º número: ')))
print(f'O maior número digitado foi {max(num)}')