'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

dec = []
for n in range(3):
    dec.append(int(input('Digite um número inteiro: ')))
dec.sort(reverse=True)
print(dec)
