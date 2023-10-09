'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

p1 = float(input('Qual o preço desse produto? R$'))
p2 = float(input('Qual o preço desse produto? R$'))
p3 = float(input('Qual o preço desse produto? R$'))
barato = p1

if p1 < p2 and p1 < p3:
    barato = p1
elif p2 < p1 and p2 < p3:
    barato = p2
elif p3 < p1 and p3 < p2:
    barato = p3

print(f'O produto a ser comprado é o de R${barato:.2f}')