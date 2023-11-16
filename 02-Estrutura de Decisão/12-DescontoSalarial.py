'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.'''

qto = float(input('Quanto você ganha por hora? R$'))
hr = int(input('Quantas horas você trabalha por mês? '))
sal = qto * hr
inss = sal * 11 / 100
sindicato = sal * 3 / 100
fgts = sal * 11 / 100

if sal <= 900:
    ir = 0
elif sal <= 1500:
    ir = sal * 5 / 100
elif sal <= 2500:
    ir = sal * 10 / 100
else:
    ir = sal * 20 / 100

print(f'Salário bruto: R${sal}')
print(f'Descnto do IR: R${ir}')
print(f'Desconto do INSS: R${inss}')
print(f'Desconto do FGTS: R${fgts}')
print (f'Total de descontos: R${fgts + inss + sindicato + ir}')
print(f'Salário liquido: R${sal - (inss + sindicato + ir)}')