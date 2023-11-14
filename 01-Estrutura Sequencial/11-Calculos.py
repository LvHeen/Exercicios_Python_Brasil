'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

from math import pow

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Outro número inteiro: '))
n3 = float(input('Agora um número real: '))
p =  (n2 / 2) * (2 * n1)
s = 3 * n1 + n3
c = n3 ** 3
print(' Primeiro número: {} \n Segundo número: {} \n Terceiro número: {}' .format(n1, n2, n3))
print(' O produto do dobro do primeiro com metade do segundo: {}\n A soma do triplo do primeiro com o terceiro: {}\n O terceiro elevado ao cubo: {:.2f}' .format(p, s, c))