'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

quanto = float(input('Quantos reais você recebe por hora? R$'))
horas= float(input('Quantas horas você trabalha por mês? '))

bruto = quanto * horas
ir = bruto * 11 / 100
inss = bruto * 8 / 100
sindicato = bruto * 5 / 100
liquido = bruto - ir - inss - sindicato

print(' - Salário Bruto: R${:.2f} \n'
       ' - IR (11%): R${:.2f} \n'
       ' - INSS (8%): R${:.2f} \n'
       ' - Sindicato (5%): R${:.2f} \n'
       ' - Salário Liquido: R${:.2f}' .format(bruto, ir, inss, sindicato, liquido))