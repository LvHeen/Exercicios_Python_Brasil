'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

Altere o programa anterior para mostrar no final a soma dos números.'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 < num2:
    for c in range(num1+1, num2):
      print(c, end=' ')
elif num2 < num1:
    for c in range(num2, num1):
       print(c, end=' ')