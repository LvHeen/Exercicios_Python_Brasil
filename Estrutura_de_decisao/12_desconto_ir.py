'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''

sal_bruto = float(input('Salário: R$'))
ir = 0
sind = (sal_bruto * 3) / 100
fgts = (sal_bruto * 11) / 100
desc = ir + sind + fgts
sal_liq = sal_bruto - (sind + ir) #FGTS não conta
porcentagem = 0

if sal_bruto <= 900:
    ir = 0
    porcentagem = 0
elif sal_bruto <= 1500:
    ir = (sal_bruto * 5) / 100
    porcentagem = 5
elif sal_bruto <= 2500:
    ir = (sal_bruto * 10) / 100
    porcentagem = 10
elif sal_bruto > 2500:
    ir = (sal_bruto * 20) / 100
    porcentagem = 20

print(f'Salário bruto: R${sal_bruto:.2f}')
print(f'IR ({porcentagem}%): R${ir}')
print(f'INSS (11%): R${fgts}')
print(f'Sindicato (3%): R${sind}')
print(f'Toral de descontos: {desc}')
print(f'Salário liquido: R${sal_liq}')