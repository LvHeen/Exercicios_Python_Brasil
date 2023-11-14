'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

qto = float(input ('Quanto você ganha por hora? R$'))
hrs = float(input ('Quantas horas por dia você trabalha? '))
mes = int(input ('Quantos dias no mês você trabalhou? '))
sal = qto * hrs * mes
print('O salário total é R${:.2f}' .format(sal))