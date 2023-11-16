'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

dia = int(input('Digite um número de 1 a 7 para aparecer o dia da semana correspondente: '))

if dia == 1:
    print('Hoje é domingo.')
elif dia == 2:
    print('Hoje é segunda-feira.')
elif dia == 3:
    print('Hoje é terça-feira.')
elif dia == 4:
    print('Hoje é quarta-feira.')
elif dia == 5:
    print('Hoje é quinta-feira.')
elif dia == 6:
    print('Hoje é sexta-feira.')
elif dia == 7:
    print('Hoje é sábado.')
else:
    print('Valor inválido.')