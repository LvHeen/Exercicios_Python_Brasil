'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação 
ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga 
se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''
from time import sleep

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
resultado = 0
par = 0
positivo = 0
inteiro = 0
decimal = 0

sleep(1)

operacao = int(input('''Qual operação você deseja realizar?
[1] soma
[2] subtração
[3] multiplicação
[4] divisão
-> '''))

'''CALCULO'''
if operacao == 1:
    resultado = n1 + n2
elif operacao == 2:
    resultado = n1 - n2
elif operacao == 3:
    resultado = n1 * n2
elif operacao == 4:
    resultado = n1 / n2

'''PAR OU IMPAR'''
if (resultado % 2) == 0:
    par = 'esse número é par'
else:
    par = 'esse número é impar'

'''POSITIVO OU NEGATIVO'''
if resultado < 0:
    positivo = 'esse número é negativo'
else:
    positivo = 'esse número é positivo'

'''INTEIRO OU DECIMAL'''
if(round(resultado) == True):
    decimal = 'esse é um número inteiro!'
else:
    decimal = 'esse é um número decimal!'

sleep(1)

print(f'O resultado foi {resultado:.2f}, {par}, {positivo} e {decimal}.')

'''Embora longo, foi um código divertido'''
