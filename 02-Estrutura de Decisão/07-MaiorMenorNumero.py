'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

n1 = int(input('Primeiro número: '))
n2 = int(input('Segudo número: '))
n3 = int(input('Terceiro número: '))

#ACHANDO O MAIOR
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

#ACHANDO O MENOR
menor = n1 
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f'O maior número é {maior} e o menor é {menor}')