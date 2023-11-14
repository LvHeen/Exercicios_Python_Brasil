'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''

num = []
for n in range(1, 6):
    num.append(int(input('Número: ')))
soma = sum(num)
media = soma / 5
print(f'A soma entre esses numeros é: {soma}')
print(f'A média entre esses números foi: {media:.2f}')
