'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês'''

valor_hora = float(input('Quanto você ganha por hora? R$'))
qtas_hora = int(input('Quantas horas você trablhou nesse mês? '))
sal = valor_hora * qtas_hora
print(f'Seu sálario esse mês foi de R${sal}')
